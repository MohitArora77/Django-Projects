from django.contrib import admin
from Modelapp.models import EmployeeModel
# Register your models here.

class EmployeeModelAdmin(admin.ModelAdmin): #class  is created to create the structure
    list_display=['id','eid','ename','company','job','esal','email','city','addr']
    # list_display_links=['ename']
admin.site.register(EmployeeModel,EmployeeModelAdmin)