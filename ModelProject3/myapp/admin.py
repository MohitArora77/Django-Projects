from django.contrib import admin

# Register your models here.
from myapp.models import StudentModel

class StudentModelAdmin(admin.ModelAdmin):
    list_display=['name','sid','phno','sal','email','addr']
    list_display_links=['sid']
admin.site.register(StudentModel,StudentModelAdmin)