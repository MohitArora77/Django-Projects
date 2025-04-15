from django.shortcuts import render

# Create your views here.
cricket_data=[
    {
        'name' : 'Ms Dhoni',
        'details':'Mahendra Singh Dhoni (born 7 July 1981) is an Indian professional cricketer who plays as a right-handed batter and a wicket-keeper. Widely regarded as one of the most prolific wicket-keeper batsmen and captains and one of the greatest ODI batsmen, he represented the Indian cricket team and was the captain of the side in limited overs formats from 2007 to 2017 and in test cricket from 2008 to 2014.'
    },
    {
        'name': 'Sachin',
        'details':'Sachin Ramesh Tendulkar (born 24 April 1973) is an Indian former international cricketer who captained the Indian national team. He is widely regarded as one of the greatest cricketers of all time,[5] and is the holder of several world records, including being the all-time highest run-scorer in both ODI and Test cricket,[6] receiving the most player of the match awards in international cricket,[7] and being the only batsman to score 100 international centuries'
    },
    {
        'name':'Kapil Dev',
        'details' : 'Kapildev Ramlal Nikhanj (born 6 January 1959) is an Indian former cricket team captain. He is regarded as one of the greatest all-rounders in the history of cricket, he was a fast-medium bowler and a hard-hitting middle-order batsman. Dev is the only player in the history of cricket to have taken more than 400 wickets (434 wickets) and scored more than 5,000 runs in Test cricket.[4]'
    },
    {
        'name' : 'Virat Kohli',
        'details':'Virat Kohli (born 5 November 1988) is an Indian international cricketer who plays Test and ODI cricket for the national team and is a former captain in all formats.He is a right-handed batsman and an occasional right arm medium pace bowler. He is called the king, the chase master and the run machine for his playing style, records and ability to lead the team to victory.Kohli is the highest run-scorer in the Indian Premier League, third in T20I, third in ODI, and third in international cricket.'
    }]
def home(request):
    return render(request,"index.html")

def cricket_views(request):
    context={'cricket':cricket_data}
    return render(request,"cricket.html",context) # loop statement to fetch the data

def football_views(request):
    return render(request,"football.html")

def hockey_views(request):
    return render(request,"hockey.html")

def sports_views(request):
    return render(request,"sports.html")