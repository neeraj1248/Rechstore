from django.db import models
from datetime import date

# Create your models here.
class Forgatetoken(models.Model):
    username = models.CharField(max_length = 100)
    date =  models.DateField(default = date.today)
    otp = models.IntegerField()
    cont = models.IntegerField(default = 1)
