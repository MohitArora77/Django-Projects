from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=50) # Compulsary argument -> Max_length
    company=models.CharField(max_length=50)
    job=models.CharField(max_length=50)
    esal=models.IntegerField()
    email=models.EmailField()
    city=models.CharField(max_length=50)
    addr=models.CharField(max_length=100)