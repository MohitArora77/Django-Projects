"""
URL configuration for MultipleAppProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from shopping_app import views as v1
# from student_app import views as v2  # To import multiple applications

urlpatterns = [
    path('admin/', admin.site.urls),
   path('shopping/',include('shopping_app.urls')),
    path('student/',include('student_app.urls')),
    
]
# '' -> can leave the name argument to get that view as default path