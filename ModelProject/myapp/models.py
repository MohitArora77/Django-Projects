from django.db import models

# Create your models here.

class StudentModel(models.Model):
    name=models.CharField(max_length=30)
    rollno=models.IntegerField()
    phno=models.IntegerField()
    addr=models.CharField(max_length=40)