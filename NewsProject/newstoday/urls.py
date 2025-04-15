from django.urls import path
from newstoday import views

urlpatterns=[
    path('news/',views.home_view),
    path('business/',views.business_news),
    path('movies/',views.movies_news),
    path('sports/',views.sports_new),
]