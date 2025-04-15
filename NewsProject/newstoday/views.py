from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'newstoday/index.html')

def business_news(request):
    msg1="Anand Mahindra hails THIS city for producing 90 ceramic, calls it 'Baahubalis' of India"
    msg2="Companies News Today highlights on March 7, 2025: Carlos Slim cuts ties with Elon Musk's Starlink, invests $22 billion in independent network"
    type="business" # type -> for specific 
    my_dict={'msg1':msg1,'msg2':msg2,'type':type}
    return render(request,'newstoday/news.html',context=my_dict)


def movies_news(request):
    msg1="Viral Video: After watching Vicky Kaushal's Chhaava movie, people in Madhya Pradesh start digging in ground for gold"
    msg2="New Tamil & Telugu Movies On OTT This Week: Full List On Latest Releases in Netflix, Amazon Prime, Zee5"
    type="movies"
    my_dict={'msg1':msg1,'msg2':msg2,'type':type}
    return render(request,'newstoday/news.html',context=my_dict)

def sports_new(request):
    msg1="Sports News Today highlights on March 1, 2025: Champions Trophy 2025 semifinals: Who will be India's opponents in last-four stage? All scenarios EXPLAINED"
    msg2="Sports News Highlights, March 7: OLY Taekwondo Champ Jones Switches To Boxing; Aravindh Nears Prague Masters Chess Title"
    type="sports"
    my_dict={'msg1':msg1,'msg2':msg2,'type':type}
    return render(request,'newstoday/news.html',context=my_dict)
    