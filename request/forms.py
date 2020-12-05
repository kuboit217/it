from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Requested
from django import forms

#tạo form làm requested
class RequestForm(forms.ModelForm):
    class Meta:
        model = Requested
        fields = '__all__'
        exclude = ['nhanvien','name','star','department','date_accept','date_closed','it_member']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    