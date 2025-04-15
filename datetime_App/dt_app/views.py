from django.shortcuts import render #render - It is a function
from django.http import HttpResponse
import datetime

# Create your views here.

def date_time(request):
    
    time=datetime.datetime.now()
    msg='<h1>Hello ,Welcome to the Django Class</h1><hr/><hr/>'
    out=msg+str(time)
    return HttpResponse(out)

def greets(request):
    c_time=datetime.datetime.now().time()
    hr=c_time.hour
    
    if hr >24 or hr==24:
        msg="Good Night"
    elif hr >18 and hr < 24 :
        msg="Good Evening"
    elif hr>12 and hr < 18:
        msg="Good Afternoon"
    elif hr>3 and hr >12:
        msg="Good Morning" 
    else:
        msg="Good Night"
    return HttpResponse(f"<h1>Greetings: {msg}<br/> Current time is :{c_time}</h1><br/> ")

def home_view(request):
    return render(request,'home.html')
#render() - It is a function , which is used to represent the final content in the web browser
# The mandatory argument is 'request'