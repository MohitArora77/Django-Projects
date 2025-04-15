from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=50)
    sid=models.IntegerField()
    phno=models.IntegerField()
    sal=models.IntegerField()
    email=models.EmailField()
    addr=models.CharField(max_length=100)
    