
import re
from django import template
from .models import User
from django.shortcuts import redirect, render
from requests import post
from .form import UserForm
# Create your views here.
def Userreg(request):
    if request.method == 'POST':
        fm=UserForm(request.POST)
        if fm.is_valid():
            try:
                fm.save()
                return redirect('/show')
            except:
                pass
    else:
        fm=UserForm()
    return render(request,'Userreg/register.html',{'form':fm})

def Home(request):
    return render(request,'Userreg/home.html')

def Show(request):
    users=User.objects.all()
    return render(request,'Userreg/show.html',{'Users':users})