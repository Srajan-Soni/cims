
from django.db import models

from home.models import City, Status

from cims.settings import BASE_DIR

import os

# Create your models here.

class Teacher(models.Model):
    def getPicPath(self, filename):
        pic_upload_path = os.path.join('teachers', str(self.id)+'_'+self.email, filename)
        return pic_upload_path

    def __str__(self):
        return self.first_name+' '+self.last_name

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=10)
    experience = models.PositiveIntegerField()
    gender = models.CharField(max_length=1)
    dob = models.DateField()
    address = models.CharField(max_length=300)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    contact = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to=getPicPath, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, default=1)
    activation_code = models.CharField(max_length=100, null=True)
    institute = models.ForeignKey(to='institutes.Institute', on_delete=models.CASCADE,default=None,null=True)

    class Meta:
        db_table = 'teachers'
