from django.shortcuts import render
from myapp.models import FeedbackModel
# Create your views here.
def feedback_view(request):
    submitted=False
    if request.method =='POST':

        Firstname=request.POST['Firstname']
        Lastname=request.POST['Lastname']
        Feedback=request.POST.get('Feedback')
        FeedbackModel.objects.create(Firstname=Firstname,Lastname=Lastname,Feedback=Feedback)
        submitted=True
    print(submitted)
    return render(request,'index.html',{'submitted':submitted})

def display_view(request):
    all_feedbacks=FeedbackModel.objects.all()
    return render(request,'retrive.html',{'all_feedbacks':all_feedbacks})