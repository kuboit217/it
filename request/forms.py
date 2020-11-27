from django.forms import ModelForm
from .models import Requested
from django import forms

#tạo form làm requested
class RequestForm(forms.ModelForm):
    class Meta:
        model = Requested
        fields = '__all__'
    