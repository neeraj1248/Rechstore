from django.db import models
from datetime import date

# Create your models here.
class Entery(models.Model):
    user_name = models.CharField(max_length = 150)
    date =  models.DateField(default = date.today)
    number = models.CharField(max_length = 15)
    name = models.CharField(max_length = 50)
    rs = models.IntegerField()
    status = models.IntegerField()
    through = models.CharField(max_length = 150,null=True,blank=True)
    payment = models.CharField(max_length = 150,null=True,blank=True)
    cb = models.IntegerField(default = 0)
    apc = models.CharField(max_length = 100,null=True,blank=True)
    remark = models.CharField(max_length = 300,null=True,blank=True)
    p_np = models.CharField(max_length = 50)
    ac_id = models.CharField(max_length = 50,null=True,blank=True)
    screenshot = models.ImageField(upload_to="screenshot",null=True,blank=True)
