from django.db import models

# Create your models here.

class Teacher(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Batch(models.Model):
    batch=models.CharField(max_length=200)
    def __str__(self):
        return self.batch

class Student(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    contact=models.IntegerField()
    batch=models.ForeignKey(Batch,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE)

