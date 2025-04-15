from django.shortcuts import render
from Modelapp.models import EmployeeModel
from django.db.models import Q,Avg,Max,Min,Sum,Count# to use combined query we import Q

# Create your views here.
def home_view(request):
    emp_data=EmployeeModel.objects.all() # fetch  the data from the database and show it in the HTML
    return render(request,'index.html',{'emp_data':emp_data})

def retrive_view(request): # to retrive specific data
    # emp_data=EmployeeModel.objects.filter(id__in=[62,63,64])
    # emp_data=EmployeeModel.objects.filter(ename__startswith='s')
    
    # to use multiple Queries at a time
    # '&' or ',' --> and '|' --> or 
    # get method is used to get specific attribute of the data (return sinlge object)
    # emp_data=EmployeeModel.objects.filter(Q(ename__startswith='s') & Q(esal__lt=40000))
    # emp_data=EmployeeModel.objects.all().order_by('eid') # For Ascending order -> we use order by
    # emp_data=EmployeeModel.objects.all().order_by('-eid') # descending order
    emp_data=EmployeeModel.objects.all().order_by('-esal') # descending order
    return render(request,'retrive.html',{'emp_data':emp_data})

def aggregate_view(request):
    avg=EmployeeModel.objects.all().aggregate(Avg('esal'))
    max=EmployeeModel.objects.all().aggregate(Max('esal'))
    min=EmployeeModel.objects.all().aggregate(Min('esal'))
    sum=EmployeeModel.objects.all().aggregate(Sum('esal'))
    count=EmployeeModel.objects.all().aggregate(Count('id'))
    emp_data={'avg':avg['esal__avg'],'max':max['esal__max'],'min':min['esal__min'],'sum':sum['esal__sum'],'count':count['id__count']}
    print(avg,max,min,sum,count,sep='\n')
    return render(request,'aggregate.html',{'emp_data':emp_data})

# max[esal__max] --> represent key of one dictionary

