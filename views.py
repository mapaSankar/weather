from django.shortcuts import render
import requests
import datetime

def index(request):
 if 'city'in request.POST:
    city=request.POST.get('city')
 else:
    city='kolkata'
 url=f'https://api.openweathermap.org/data/2.5/weather?q={city }&appid=4683b8bebcbc9a9323c1090d30eaba6b'
 PARAMS={'units':'metric'}
 data=requests.get(url,PARAMS).json()

 description=data['weather'][0]['description']
 icon=data['weather'][0]['icon']
 temp=data['main']['temp']
 day=datetime.datetime.now()

 return render(request,'index.html',{'description':description,
                                     'icon':icon,
                                     'temp':temp,
                                     'day':day,
                                     'city':city})
