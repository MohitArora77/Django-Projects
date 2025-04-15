from django.urls import path
from student_app import views

urlpatterns = [
    path('attendace/',views.attendance_view),
    path('exam/',views.exam_view),
    path('leave/',views.leave_view),]