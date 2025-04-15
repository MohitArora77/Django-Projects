from django.shortcuts import render
import datetime
import random

# Create your views here.
def display_view(request):
    time=datetime.datetime.now().time()
    hr=time.hour
     
    if hr >24 or hr==24:
        s="Good Night"
    elif hr >18 and hr < 24 :
        s="Good Evening"
    elif hr>12 and hr < 18:
        s="Good Afternoon"
    elif hr>3 and hr >12:
        s="Good Morning" 
    else:
        s="Good Night"
 
    msg_list=[
        'Golden Days Ahead',
        'Very soon you are going to get a Job',
        'Watch reels before sleep',
        'Avoid water drink beer',
        'Sleep more even if it is a class',
        'Better to smoke at home rather than outside'
        
    ]
    
    name_list=['Shresth','Abhishek','Mohit','Kanishq','Jay','Rahul','Kunal']
    candidate_list=['Tamanna','Nora','Sunny','Shradha','Sheela']
    
    name=random.choice(name_list)
    candidate=random.choice(candidate_list)
    msg=random.choice(msg_list)
    
    my_dict={'time':time,'Greet':s,'name':name,'candidate':candidate,'msg':msg}
    
    
    return render(request,'astroapp/index.html',context=my_dict)