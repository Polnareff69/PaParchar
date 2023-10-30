from django import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User   


class CreateUserForm(UserCreationForm):
    phone_number = forms.CharField(max_length=12)
    class Meta:
        model = User
        fields = ['username','first_name','email','phone_number','password1','password2']
