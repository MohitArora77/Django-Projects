from django.urls import path
from DTL_app import views

urlpatterns=[
    path('time/',views.time_view),
]