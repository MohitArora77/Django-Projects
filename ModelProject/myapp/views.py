from django.shortcuts import render
from myapp.models import StudentModel
# Create your views here.
def student_view(request):
    student_data=StudentModel.objects.all()
    context={'student_data':student_data} # command used to connect with the frontend
    # print(list(student_data))
    return render(request,'student.html',context)

# Query set -> list format output -> for Frontend
# list will be send to the html page