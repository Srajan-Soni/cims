from django.db import models

from django.contrib.auth.models import User
from django.forms import widgets

from home.models import City,Status

from teachers.models import Teacher

import os

# Create your models here.
class Institute(models.Model):
    def get_upload_path(self, filename):
        user = User.objects.get(id=self.user_id)
        upload_path = os.path.join('institutes', user.username, filename)
        return upload_path

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    contact = models.CharField(max_length=10)
    activation_code = models.CharField(max_length=20, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, default=2)
    details = models.CharField(max_length=2000, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, null=True)
    start_date = models.DateField(null=True)
    logo = models.ImageField(upload_to=get_upload_path, null=True)
    
    class Meta:
        db_table = 'institutes'


class PicType(models.Model):
    pic_type = models.CharField(max_length=20)

    class Meta:
        db_table = 'pic_types'


class InstitutePic(models.Model):
    def get_upload_path(self, filename):
        user = User.objects.get(id=self.institute_id)
        pic_type_obj = PicType.objects.get(id=self.pictype_id)
        folder = pic_type_obj.pic_type
        upload_path = os.path.join('institutes', user.username, 'institute_pics', folder, filename)
        return upload_path

    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    pic_path = models.ImageField(upload_to=get_upload_path)
    pictype = models.ForeignKey(PicType, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        db_table = 'institute_pics'


class Course(models.Model):
    def get_file_upload_path(self, filename):
        user = User.objects.get(id=self.institute_id)
        course_name = self.name.replace(' ','_').capitalize()
        course_file_upload_path = os.path.join('institutes', user.username, 'courses', course_name, filename)

        return course_file_upload_path

    def __str__(self):
        return self.name
        
    name = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=80)
    details = models.CharField(max_length=2000)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    syllabus = models.FileField(upload_to=get_file_upload_path, null=True)
    course_pic = models.ImageField(upload_to=get_file_upload_path, null=True)
    star_rank = models.IntegerField(default=0,null=True)
    star_rank_count = models.IntegerField(default=0,null=True)

    class Meta:
        db_table = 'courses'


class Batch(models.Model):
    batch_name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    mode = models.BooleanField()
    frequency = models.BooleanField()
    start_date = models.DateField()
    duration = models.PositiveIntegerField()
    start_time = models.TimeField()
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, default=4)
    student_count = models.IntegerField(default=0)
    course_fees = models.PositiveIntegerField()
    concession = models.PositiveIntegerField()

    class Meta:
        db_table = 'batches' 
