from django.urls import path
from myapp import views

urlpatterns=[
    path("student/",views.student_view),
]