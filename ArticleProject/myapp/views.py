from django.shortcuts import render
from myapp.models import ArticleModel
# Create your views here.
def form_view(request):
    if request.method =='POST':
        Title=request.POST['Title']
        Description=request.POST.get('Description')
        ArticleModel.objects.create(Title=Title,Description=Description)
    return render(request,'form.html')

def display_view(request):
   all_articles=ArticleModel.objects.all()
   return render(request,'articles.html',{'all_articles':all_articles})

def display_specific_view(request,id):
    spec_data=ArticleModel.objects.get(id=id)
    print(spec_data.Title)
    print(spec_data.Description)
    return render (request,'specific.html',{'spec_data':spec_data})