from django.db import models

# Create your models here.
class Numbers(models.Model):
    username = models.CharField(max_length= 150,null= True,blank = True)
    number = models.CharField(max_length = 15)
    name = models.CharField(max_length = 50)
    ac_id = models.CharField(max_length = 50)
