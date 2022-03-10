from teachers.models import Teacher
from django.http.response import HttpResponse
from home.utils import collectAllCities
from django.shortcuts import render
from cims.settings import BASE_DIR 
import os

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def teacher_pic_upload_view(request):
    flag = True

    filename = request.FILES.get('file')
    print(str(filename),' ###   ~~~~~  ###')
    teacher_id = request.session.get('teacher_id')
    try:
        teacher = Teacher.objects.get(id=teacher_id)
        teacher.profile_pic = filename
        teacher.save()
    except:
        flag = False

    return HttpResponse(flag)


@login_required
def add_teacher_view(request):
    flag = True
    gd = request.GET    
    
    try:
        teacher = Teacher(first_name=gd.get('first_name'),
                            last_name=gd.get('last_name'),
                            email=gd.get('email'),
                            password=gd.get('password'),
                            gender=gd.get('gender'),
                            dob=gd.get('dob'),
                            address=gd.get('address'),
                            city_id=gd.get('city_id'),
                            contact=gd.get('contact'),
                            qualification=gd.get('qualification'),
                            experience=gd.get('experience'),
                            institute_id=request.session.get('_auth_user_id'))
        teacher.save()
    except: 
        flag = False

    request.session['teacher_id'] = teacher.id

    teacher_folder = os.path.join(BASE_DIR,'static/media/teachers',str(teacher.id)+'_'+teacher.email)
    
    os.mkdir(teacher_folder)
    
    return HttpResponse(flag)


@login_required
def teacher_view(request):
    cities = collectAllCities()

    institute_id = request.session.get('_auth_user_id')
    teachers = Teacher.objects.filter(institute_id=institute_id)

    context_data = {'all_cities': cities, 'all_teachers': teachers}

    return render(request, 'teachers/teachers.html', context_data)






