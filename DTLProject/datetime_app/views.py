from django.shortcuts import render
import datetime

# Create your views here.

def time_view(request):
    time=datetime.datetime.now()
    my_dict={'data':time}
    return render(request,'time.html',context=my_dict) # Context - it is a dictionary
    # return render(request,'time.html',my_dict)