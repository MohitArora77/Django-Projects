from django.shortcuts import render
from myapp.models import ArticleModel
# Create your views here.
def form_view(request):
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST.get('desc')
        ArticleModel.objects.create(title=title,desc=desc)
    return render(request,'form.html')

def article_view(request):
    all_articles=ArticleModel.objects.all()
    return render(request,'article.html',{'all_articles':all_articles})

def specific_view(request,id):
    spec_data=ArticleModel.objects.get(id=id)
    print(spec_data.title)
    print(spec_data.desc)
    return render(request,'specific.html',{'spec_data':spec_data})