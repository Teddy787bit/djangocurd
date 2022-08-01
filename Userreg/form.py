

from os import uname
import django

from django import forms
from django.core import validators
from django import template
from .models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ('uname','email','phone')
        