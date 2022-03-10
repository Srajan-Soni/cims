from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from institutes.models import Batch, Course, Institute, InstitutePic

from institutes.forms import BatchForm, ProfileForm

from home.forms import SignupForm 

from home.utils import reCaptchaTest

from django.http import HttpResponse

import os

from cims.settings import BASE_DIR

import random

import json

# Create your views here.
####################################################################
def search_view(request):
    search_key = request.GET.get('search_key');
    city_id = request.GET.get('student_city')

    batches = Batch.objects.filter(batch_name__icontains=search_key, course__institute__city_id=int(city_id))
       
    return render(request, 'students/search_result.html', {'all_batches': batches})



@login_required
def batches_view(request):
    institute_id = request.session.get('_auth_user_id')

    if request.method == 'POST':
        batch_name = request.POST.get('batch_name')
        course = request.POST.get('course')
        mode = request.POST.get('mode')
        frequency = request.POST.get('frequency')
        start_date = request.POST.get('start_date')
        duration = request.POST.get('duration')
        start_time = request.POST.get('start_time')
        teacher = request.POST.get('teacher')
        course_fees = request.POST.get('course_fees')
        concession = request.POST.get('concession')
        
        #validation code
               
        batch = Batch(batch_name=batch_name,course_id=course,mode=(True if mode=='true' else False),frequency=(True if frequency=='true' else False),start_date=start_date,duration=duration,start_time=start_time,teacher_id=teacher,course_fees=course_fees,concession=concession)
        batch.save()

        return redirect('/institutes/batches')
    else:
        batch_form = BatchForm(inst_id=institute_id)

        batches = Batch.objects.filter(course__institute_id=request.session.get('_auth_user_id'))
        print(batches.query,'++++')
        return render(request, 'institutes/batches.html', {'form': batch_form, 'all_batches': batches})    

    


@login_required
def course_syllabus_upload_view(request):
    file_path = request.FILES.get('file')
    course_id = request.session.get('course_id')
    course = Course.objects.get(id=course_id)
    course.syllabus = file_path

    try:
        course.save()        
    except:
        return HttpResponse('false')

    return HttpResponse('done')


@login_required
def course_pic_upload_view(request):
    file_path = request.FILES.get('file')
    course_id = request.session.get('course_id')
    course = Course.objects.get(id=course_id)
    course.course_pic = file_path

    try:
        course.save()        
    except:
        return HttpResponse('false')

    return HttpResponse('done')
    

@login_required
def courses_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
         
        institute_id = request.session.get('_auth_user_id')
        user = User.objects.get(id=institute_id)

        course_name = data.get('course_name')
        course_subtitle = data.get('course_subtitle')
        course_details = data.get('course_details')

        course = Course(institute_id=institute_id, name=course_name, subtitle=course_subtitle, details=course_details)
        
        try:
            course.save()

            print(course.pk, '### ---------------------------------------- ###')

            course_folder = course_name.replace(' ', '_').upper()
            course_folder_path = os.path.join(BASE_DIR, 'static', 'media', 'institutes', user.username, 'courses', course_folder)
            os.mkdir(course_folder_path)

            request.session['course_id'] = course.id

            return HttpResponse(course_name)
        except Exception as msg:
            print(msg)
            return HttpResponse('false')
            
    else:
        institute_id = request.session.get('_auth_user_id')

        courses = Course.objects.filter(institute_id=institute_id)
        
        return render(request, 'institutes/courses.html', {'all_courses': courses})


@login_required
def institute_pics_upload_view(request, pic_type_id):
    pic = request.FILES.get('file')
    
    user_id = request.session.get('_auth_user_id')

    institute_pic = InstitutePic(pic_path=pic, institute_id=user_id, pictype_id=pic_type_id)
    institute_pic.save()

    return redirect('/institutes/pics')

@login_required
def pics_view(request):
    institute_id = request.session.get('_auth_user_id')

    interior_pics = list(InstitutePic.objects.filter(institute_id=institute_id, pictype_id=1))
    exterior_pics = list(InstitutePic.objects.filter(institute_id=institute_id, pictype_id=2))
    lab_pics = list(InstitutePic.objects.filter(institute_id=institute_id, pictype_id=3))
    library_pics = list(InstitutePic.objects.filter(institute_id=institute_id, pictype_id=4))
    classroom_pics = list(InstitutePic.objects.filter(institute_id=institute_id, pictype_id=5))
    office_pics = list(InstitutePic.objects.filter(institute_id=institute_id, pictype_id=6))
    parking_pics = list(InstitutePic.objects.filter(institute_id=institute_id, pictype_id=7))
    sportsarea_pics = list(InstitutePic.objects.filter(institute_id=institute_id, pictype_id=8))
    facultyroom_pics = list(InstitutePic.objects.filter(institute_id=institute_id, pictype_id=9))

    data = {
            'interior_pics': interior_pics, 
            'exterior_pics': exterior_pics,
            'lab_pics': lab_pics,
            'library_pics': library_pics,
            'classroom_pics': classroom_pics,
            'office_pics': office_pics,
            'parking_pics': parking_pics,
            'sportsarea_pics': sportsarea_pics,
            'facultyroom_pics': facultyroom_pics,
           }

    return render(request, 'institutes/pics.html', data)


@login_required
def dashboard_view(request):
    return render(request, 'institutes/dashboard.html')

@login_required
def profile_logo_upload_view(request):
    user_id = request.session.get('_auth_user_id')
    institute = Institute.objects.get(user_id=user_id)
    try:
        old_pic = os.path.join(BASE_DIR, 'static/'+institute.logo.url)
        os.remove(old_pic)
    except:
        print('Error ++++++++++++++++++++')

    logo = request.FILES.get('file')
    institute.logo = logo
    institute.save()

    request.session['logo'] = institute.logo.url

    return redirect('/institutes/profile')


@login_required
def profile_view(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)

        print(profile_form)
        
        if profile_form.is_valid():
            institute = profile_form.save(commit=False)
            institute.user_id = request.session.get('_auth_user_id')
            institute.status_id = 1
            institute.save()           

        return render(request, 'institutes/profile_form.html',  {'form': profile_form})
    else:
        user_id = request.session.get('_auth_user_id')
        institute = Institute.objects.get(user_id=user_id)
        
        profile_form = ProfileForm(initial={'name': institute.name, 'details': institute.details, 'start_date': institute.start_date, 'address': institute.address, 'city': institute.city_id, 'contact': institute.contact})
        
        return render(request, 'institutes/profile_form.html', {'form': profile_form})


# def login_view(request):
#     reCaptchaTestResult = reCaptchaTest(request)
#     if reCaptchaTestResult:
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         login_as = request.POST.get('login_as')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             institute = Institute.objects.get(user_id=user.pk)
#             #institute = Institute.objects.get(user=user)

#             try:
#                 request.session['logo'] = institute.logo.url
#             except ValueError:
#                 pass

#             status_id = institute.status_id

#             if status_id == 3:
#                 return redirect('/institutes/profile')
#             elif status_id == 2:
#                 return redirect('/home')
#             elif status_id == 1:
#                 return redirect('/institutes/dashboard')           
#         else:
#             return redirect('/accounts/login')
#     else:
#         return redirect('/accounts/login')
        

#TemplateView a class based view used instead. check institutes>urls.py
# def signup_success_view(request):
#     return render(request, 'institutes/signup_success.html')


def activate_account_view(request):
    username = request.GET.get('username')
    activation_code = request.GET.get('activation_code')

    user = User.objects.get(username=username)

    try:
        institute = Institute.objects.get(user=user, activation_code=activation_code)
        institute.status_id = 3   #status_id-3: first time login
        institute.activation_code = None

        institute.save()
    
        return redirect('/accounts/login')
    except:
        return render(request, 'index.html')    
    

# def check_username_view(request):
#     uname = request.GET.get('username')
#     flag = True

#     try:
#         user = User.objects.get(username=uname)
#     except:
#         flag = False

#     return HttpResponse(flag)


# def signup_view(request):
#     if request.method == 'POST':
#         recaptcha_test_result = reCaptchaTest(request)

#         if recaptcha_test_result:
#             signup_form = SignupForm(request.POST)
#             if signup_form.is_valid():
#                 user = signup_form.save(commit=False)
#                 user.set_password(user.password)
#                 user.save()

#                 contact = request.POST.get('contact')
#                 activation_code = random.randrange(11111111,99999999)
#                 institute = Institute(user=user, contact=contact, activation_code=activation_code)
#                 institute.save()

#                 institute_folder = os.path.join(BASE_DIR, 'static/media/institutes/'+user.username)
#                 os.mkdir(institute_folder)
#                 os.mkdir(institute_folder+'/institute_pics')
#                 institute_pics_folder = os.path.join(institute_folder, 'institute_pics')

#                 os.mkdir(institute_pics_folder+'/interior')
#                 os.mkdir(institute_pics_folder+'/exterior')
#                 os.mkdir(institute_pics_folder+'/lab')
#                 os.mkdir(institute_pics_folder+'/library')
#                 os.mkdir(institute_pics_folder+'/classroom')
#                 os.mkdir(institute_pics_folder+'/office')
#                 os.mkdir(institute_pics_folder+'/parking')
#                 os.mkdir(institute_pics_folder+'/sportsarea')
#                 os.mkdir(institute_pics_folder+'/facultyroom')

#                 os.mkdir(institute_folder+'/courses')

#                 #subject = 'Activate Your Account'
#                 #sender = 'dinesh22922@gmail.com'
                
#                 #message = account_activation_mail(user.username, activation_code)
                
#                 #send_mail(subject, '', sender, [user.email], fail_silently=False, html_message=message)                

#                 return redirect('/institutes/signup_success')
#             else:
#                 return render(request, 'institutes/signup.html', {'form' : signup_form, 'validation' : False})
#         else:
#             return redirect('/home')
#     else:
#         signup_form = SignupForm()
#         return render(request, 'institutes/signup.html', {'form' : signup_form, 'validation' : True})