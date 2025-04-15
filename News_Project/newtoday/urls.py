from django.urls import path
from newtoday import views

urlpatterns=[
     path('',views.home),
     path('business/',views.business_news),
     path('movies/',views.movies_news),
     path('sports/',views.sports_news),
 ]