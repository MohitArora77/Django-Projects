from django.urls import path
from datetime_app import views

urlpatterns=[
    path('time/',views.time_view)
]