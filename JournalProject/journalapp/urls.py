from django.urls import path # path is a function
from journalapp import views # views is a method 

urlpatterns=[
    path("",views.home),
    path("cricket/",views.cricket_views, name='cricket'),
    path("football/",views.football_views,name='football'),
    path("hockey/",views.hockey_views ,name='hockey'),
    path("sports/",views.sports_views)
] 