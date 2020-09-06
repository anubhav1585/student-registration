from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Studentinfo


class Signup(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name',]
        widget = {'username': forms.Textarea(attrs= {'class': 'form-control'}),
                    'first_name': forms.Textarea(attrs= {'class': 'form-control'}),
                    'last_name': forms.Textarea(attrs= {'class': 'form-control'}),}


class Student(forms.ModelForm):
    class Meta:
        model = Studentinfo
        fields = ['name','father_n' ,'mother_n' ,'course','address' ]
        labels = {'father_n':"father's name" ,'mother_n':"mother's name"}
