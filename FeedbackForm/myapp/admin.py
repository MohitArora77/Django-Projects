from django.contrib import admin
from myapp.models import FeedbackModel

# Register your models here.
class FeedbackModelAdmin(admin.ModelAdmin):
    list_display=['Firstname','Lastname','Feedback']
    
admin.site.register(FeedbackModel,FeedbackModelAdmin)