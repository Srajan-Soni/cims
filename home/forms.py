from django import forms

from django.contrib.auth.models import User

import re

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    contact = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        uname = self.cleaned_data['username']

        if not re.search('^[a-zA-Z\d_]{5,15}$', uname):
            raise forms.ValidationError('Invalid Username... !')

        return uname

    def clean_email(self):
        email = self.cleaned_data['email']

        if not re.search('^([a-zA-Z\d\._-]+)@([a-zA-Z\d_-]{2,})\.([a-zA-Z]{2,5})(\.[a-zA-Z]{2,5})?$', email):
            raise forms.ValidationError('Invalid Email...!')

        return email

    def clean_password(self):
        password = self.cleaned_data['password']

        if not re.search('^[a-zA-Z\d_-]{8,20}$', password):
            raise forms.ValidationError('Invalid Password...!')

        return password

    def clean_contact(self):
        contact = self.cleaned_data['contact']

        if not re.search('^[5-9][0-9]{9}$', contact):
            raise forms.ValidationError('Invalid Contact...!')

        return contact