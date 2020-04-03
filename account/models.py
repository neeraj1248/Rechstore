from django.db import models
from datetime import date

# Create your models here.
class Accounts(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 70)
    phone = models.CharField(max_length = 15)
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 20)

class Token(models.Model):
    username = models.CharField(max_length=30)
    date =  models.DateField(default = date.today)
    name = models.CharField(max_length = 30, null= True, blank = True)
    email = models.CharField(max_length = 70, null= True, blank = True)
    phone = models.CharField(max_length = 15, null= True, blank = True)
    password = models.CharField(max_length = 20, null= True, blank = True)
    token = models.CharField(max_length = 100)
    otp = models.IntegerField()
    cont = models.IntegerField(default = 1)
