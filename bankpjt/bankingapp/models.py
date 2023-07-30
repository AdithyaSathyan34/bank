
from django.db import models

# Create your models here.
class bank_detail(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    dob = models.DateTimeField()
    mail = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    accounttype = models.CharField(max_length=100)
    material = models.CharField(max_length=100)

