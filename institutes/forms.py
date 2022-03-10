from teachers.models import Teacher
from institutes.utils import prepareCourseList
from django import forms

from django.contrib.auth.models import User
from django.forms.widgets import TextInput, Textarea

from institutes.models import Batch, Course, Institute
from home.models import City

import re

from home.utils import prepareCityList

class BatchForm(forms.ModelForm):    
    class Meta:
        model = Batch
        fields = ('batch_name', 'course', 'mode', 'frequency', 'start_date', 'duration', 'start_time', 'teacher', 'course_fees', 'concession')

    batch_name = forms.CharField(widget=TextInput(attrs={'class': 'form-control'})) 
    mode = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input'}), choices=[('true','Online'), ('false','Offline')])   
    frequency = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class': 'form-check-input'}), choices=[('true','Regular'), ('false', 'Alternate Days')])
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date' ,'class': 'form-control'}))
    duration = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time','class': 'form-control'}))
    course_fees = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    concession = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    def __init__(self, inst_id, *args, **kwargs):
        super(BatchForm, self).__init__(*args, **kwargs)          
        self.fields['course'].queryset = Course.objects.filter(institute_id=inst_id)
        self.fields['course'].widget.attrs['class'] = 'form-control'
        self.fields['teacher'].queryset = Teacher.objects.filter(institute_id=inst_id)
        self.fields['teacher'].widget.attrs['class'] = 'form-control';

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Institute
        fields = ('name', 'details', 'start_date', 'address', 'city', 'contact')
    
    name = forms.CharField(widget=TextInput(attrs={'class': 'form-control', 'maxlength': '50'}))
    details = forms.CharField(widget=Textarea(attrs={'rows': '5', 'class': 'form-control'}))
    address = forms.CharField(widget=Textarea(attrs={'rows': '3', 'class': 'form-control'}))
    cities = prepareCityList()    
    city = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=cities)
    contact = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))

    def clean_city(self):
        city_id = self.cleaned_data['city'] 
        return City(id=city_id)


# class SignupForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')

#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     contact = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

#     def clean_username(self):
#         uname = self.cleaned_data['username']

#         if not re.search('^[a-zA-Z\d_]{5,15}$', uname):
#             raise forms.ValidationError('Invalid Username... !')

#         return uname

#     def clean_email(self):
#         email = self.cleaned_data['email']

#         if not re.search('^([a-zA-Z\d\._-]+)@([a-zA-Z\d_-]{2,})\.([a-zA-Z]{2,5})(\.[a-zA-Z]{2,5})?$', email):
#             raise forms.ValidationError('Invalid Email...!')

#         return email

#     def clean_password(self):
#         password = self.cleaned_data['password']

#         if not re.search('^[a-zA-Z\d_-]{8,20}$', password):
#             raise forms.ValidationError('Invalid Password...!')

#         return password

#     def clean_contact(self):
#         contact = self.cleaned_data['contact']

#         if not re.search('^[5-9][0-9]{9}$', contact):
#             raise forms.ValidationError('Invalid Contact...!')

#         return contact