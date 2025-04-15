from django.urls import path
from Modelapp import views

urlpatterns=[
    path('home/',views.home_view),
    path('retrive/',views.retrive_view),
    path('aggregate/',views.aggregate_view)
]