from django.urls import path
from astroapp import views


urlpatterns = [
    path('display/',views.display_view)
]
