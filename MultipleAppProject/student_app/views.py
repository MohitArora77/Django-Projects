from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def attendance_view(request):
    return HttpResponse("<h1>Student Attendance</h1>")

def exam_view(request):
    return HttpResponse("<h1>Exams Date</h1>")

def leave_view(request):
    return HttpResponse("<h1>Please Leave</h1>")