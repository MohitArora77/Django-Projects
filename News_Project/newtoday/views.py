from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"newsapp/index.html")

def business_news(request):
    msg1="1.) As the new financial year (FY 2025-26) approaches, taxpayers need to make a choice between the old and new tax regimes. Though both regimes are equally good with their own set of advantages, the ideal option depends upon the income, deductions, and fiscal goals of a taxpayer."
    msg2="2.) MUMBAI: The rupee on Friday regained 85 level, posting its strongest gain against the dollar in over a month, supported by foreign fund inflows and the unwinding of speculative long-dollar positions. Meanwhile, the sensex and Nifty both continued their northward movements and closed higher, their fifth consecutive sessions of gains."
    type="Business" # type -> for specific 
    my_dict={'msg1':msg1,'msg2':msg2,'type':type}
    return render(request,'newsapp/news.html',context=my_dict)


def movies_news(request):
    msg1="1.) Latest OTT Releases This Week: 22 new web series and movies to watch on Netflix, Amazon Prime Video, and more"
    msg2="2.) A beginners guide to gripping serial killer movies available on Amazon Prime Video, Netflix and YouTube"    
    type="Movies"
    my_dict={'msg1':msg1,'msg2':msg2,'type':type}
    return render(request,'newsapp/news.html',context=my_dict)

def sports_news(request):
    msg1="1.) CHENNAI: In the first 17 editions of the Indian Premier League (IPL), Chennai Super Kings (five), Mumbai Indians (five) and Kolkata Knight Riders (3) have taken home the crown 13 times between them. Royal Challengers Bengaluru, one of the founding eight, have underachieved. Even if they reached the final three times, they have ended up on the losing all side on all of those occasions."
    msg2="2.) The story of Gautam Gambhir and Kolkata Knight Riders (KKR) has been nothing short of a fairytale. No matter the role he played within the team, KKR always seemed to perform well in his presence. After failing to make the playoffs in their first three seasons, KKR won the title in 2012 and 2014, following Gambhir's arrival in 2011."
    type="Sports"
    my_dict={'msg1':msg1,'msg2':msg2,'type':type}
    return render(request,'newsapp/news.html',context=my_dict)