from django.db import models

# Create your models here.
class Customer(models.Model):
    user_name = models.CharField(max_length = 150)
    number = models.CharField(max_length = 15,null=True, blank = True)
    name = models.CharField(max_length = 150,null=True, blank = True)
    ac_id = models.CharField(max_length = 100,null=True, blank = True)
    balance = models.IntegerField(default = 0,null=True, blank = True)
