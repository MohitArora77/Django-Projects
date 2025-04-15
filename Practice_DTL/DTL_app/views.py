from django.shortcuts import render
import datetime
# Create your views here.

def time_view(request):
    time=datetime.datetime.now()
    s_name="ABC"
    rollno=45
    mock_rating=1
    my_dict={'data':time,'name':s_name,'rollno':rollno,'rating':mock_rating}
    list1=[
        {'name':'Sachin Tendulkar', 'Jersy':10,'sports':'Cricket'},
         {'name':'Ronaldo', 'Jersy':7,'sports':'Footbal'},
          {'name':'Kobi', 'Jersy':10,'sports':'Basket Ball'},
    ]
    my_dict={'list1':list1}
    return render(request,'info.html',context=my_dict)