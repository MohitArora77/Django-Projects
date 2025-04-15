from django.urls import path
from myapp import views

urlpatterns=[
    path('home/',views.feedback_view,name='form'),
    path('display/',views.display_view,name='feedbacks')
]