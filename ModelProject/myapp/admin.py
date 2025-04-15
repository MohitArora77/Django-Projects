from django.contrib import admin
from myapp.models import StudentModel
# Register your models here.

class StudentModelAdmin(admin.ModelAdmin):
    list_display=['rollno','name','phno','addr']
    
    # to create another attribute as a link
    # list_display_links=['name']
    
admin.site.register(StudentModel,StudentModelAdmin)