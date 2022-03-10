from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from home.utils import prepareCityList, sendOTP
from home.models import City
from home.utils import reCaptchaTest 
from home.forms import SignupForm

from institutes.models import Institute
from students.models import Student

import os, random, json

from cims.settings import BASE_DIR

# Create your views here.
def user_city_view(request):
    uid = request.session.get('_auth_user_id')

    city_id = None

    try:
        city_id = Institute.objects.get(user_id=uid).city_id
    except:
        try:
            city_id = Student.objects.get(user_id=uid).city_id
        except:
            pass
    
    return HttpResponse(city_id)




def login_view(request):
    reCaptchaTestResult = reCaptchaTest(request)
    if reCaptchaTestResult:
        username = request.POST.get('username')
        password = request.POST.get('password')
        login_as = int(request.POST.get('login_as'))

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if login_as == 2:
                institute = Institute.objects.get(user_id=user.pk)
                #institute = Institute.objects.get(user=user)

                try:
                    request.session['logo'] = institute.logo.url
                except ValueError:
                    pass

                status_id = institute.status_id

                if status_id == 3:
                    return redirect('/institutes/profile')
                elif status_id == 2:
                    return redirect('/home')
                elif status_id == 1:
                    return redirect('/institutes/dashboard')           
            elif login_as == 1:
                return redirect('/students/dashboard')
            else:
               pass 
        else:
            return redirect('/accounts/login')
    else:
        return redirect('/accounts/login')


def check_username_view(request):
    uname = request.GET.get('username')
    flag = True

    try:
        user = User.objects.get(username=uname)
    except:
        flag = False

    return HttpResponse(flag)


def signup_view(request):
    if request.method == 'POST':
        recaptcha_test_result = reCaptchaTest(request)

        if recaptcha_test_result:
            signup_form = SignupForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save(commit=False)
                user.set_password(user.password)
                user.save()

                contact = request.POST.get('contact')
                activation_code = random.randrange(11111111,99999999)

                signup_as = request.POST.get('signup_as')
                
                if signup_as == '2':
                    #-----------------------------------
                    institute = Institute(user=user, contact=contact, activation_code=activation_code)
                    institute.save()

                    institute_folder = os.path.join(BASE_DIR, 'static/media/institutes/'+user.username)
                    os.mkdir(institute_folder)
                    os.mkdir(institute_folder+'/institute_pics')
                    institute_pics_folder = os.path.join(institute_folder, 'institute_pics')

                    os.mkdir(institute_pics_folder+'/interior')
                    os.mkdir(institute_pics_folder+'/exterior')
                    os.mkdir(institute_pics_folder+'/lab')
                    os.mkdir(institute_pics_folder+'/library')
                    os.mkdir(institute_pics_folder+'/classroom')
                    os.mkdir(institute_pics_folder+'/office')
                    os.mkdir(institute_pics_folder+'/parking')
                    os.mkdir(institute_pics_folder+'/sportsarea')
                    os.mkdir(institute_pics_folder+'/facultyroom')

                    os.mkdir(institute_folder+'/courses')
                    #-----------------------------------------
                else:
                    student = Student(user=user, contact=contact, activation_code=activation_code)
                    student.save()
                    student_folder = os.path.join(BASE_DIR, 'static/media/students/'+user.username)
                    os.mkdir(student_folder)

                #subject = 'Activate Your Account'
                #sender = 'dinesh22922@gmail.com'
                
                #message = account_activation_mail(user.username, activation_code)
                
                #send_mail(subject, '', sender, [user.email], fail_silently=False, html_message=message)                

                return redirect('/home/signup_success')
            else:
                return render(request, 'signup.html', {'form' : signup_form, 'validation' : False})
        else:
            return redirect('/home')
    else:
        signup_form = SignupForm()
        return render(request, 'signup.html', {'form' : signup_form, 'validation' : True})


def city_list_view(request):
    cities = City.objects.all()

    srdata = serializers.serialize('json', cities)
    res = json.loads(srdata)

    return HttpResponse(json.dumps(res))


@login_required
def check_otp_view(request):
    received_otp = request.GET.get('otp')
    saved_otp = str(request.session.get('otp'))

    print(received_otp, saved_otp)

    result = saved_otp == received_otp

    #return HttpResponse(result)
    return HttpResponse(True)


@login_required
def send_otp_view(request):
    #status = sendOTP(request)
    status = 'sent'

    return HttpResponse(status)



def index_view(request):
    return render(request, 'index.html')