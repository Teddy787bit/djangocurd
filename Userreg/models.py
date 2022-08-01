from os import uname
from django.db import models

# Create your models here.
class User(models.Model):
    uname= models.CharField(max_length=70)
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=10)