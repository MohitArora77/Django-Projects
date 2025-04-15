from django.db import models

# Create your models here.
class FeedbackModel(models.Model):
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Feedback=models.TextField()
    