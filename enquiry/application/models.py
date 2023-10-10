from django.db import models

# Create your models here.

class Enquiry(models.Model):
    name=models.CharField(max_length=200)
    adress=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)

