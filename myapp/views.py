from django.shortcuts import render
import requests
# Create your views here.
def main(request):
    r = requests.get('http://api.mediastack.com/v1/news?access_key=59b35f78e20f5b684af8678b2b785fad&countries=es')
    res=r.json()
    data = res['data']
    title = []
    description = []
    image = []
    url = []
    for i in data:
        if (i['image'] !=' '):
            title.append(i['title'])
            description.append(i['description'])
            image.append(i['image'])
            url.append(i['url'])
    news = zip(title,description,image,url)
    # it would basically make a list containing each of the elements tuple like [(t1,d1,i1,u1),(t2,d2,i2,u2)]
    return render(request,'index.html',{'news':news})

def home(request):
    return render(request,'home.html')