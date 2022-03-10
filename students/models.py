from django.db import models

from django.contrib.auth.models import User
from home.models import Status, City

# Create your models here.
class Student(models.Model):
    def get_upload_path(self, filename):
        pass

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    contact = models.CharField(max_length=10)
    activation_code = models.CharField(max_length=20, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, default=2)
    about_me = models.CharField(max_length=500, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50, null=True)
    dob = models.DateField(null=True)
    profile_pic = models.ImageField(upload_to=get_upload_path, null=True)
    gender = models.BooleanField(null=True)

    class Meta:
        db_table = 'students'