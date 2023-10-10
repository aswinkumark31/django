from django.db import models

# Create your models here.

class Department(models.Model):
    dept=models.CharField(max_length=200)

    def __str__(self):
        return self.dept

class Student(models.Model):
    name=models.CharField(max_length=200)
    course=models.CharField(max_length=200)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
