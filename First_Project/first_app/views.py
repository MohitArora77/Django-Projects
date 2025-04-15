from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# To create view we need function
def home_view(request): #request is mandatory but we can use other variable as well.
    return render(request,'base.html') #by using render we can connect html file with view

