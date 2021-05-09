from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf.urls import url
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# Create your views here.
def home(request):
    title='Wearever'
    owm = OWM('47005e466640dd018e9b1e79039f299c')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Stony Brook, US')
    w = observation.weather
    html = render_to_string('home.html', {'title': title, 'stat': w.detailed_status, 'temp': w.temperature('fahrenheit').get('temp'), 'humid': w.humidity, 'wind': w.wind().get('speed')})
    return HttpResponse(html)

def about(request):
    group = 'Inverse Intelligence'
    title='Wearever'
    html = render_to_string('about.html', {'title': title, 'group': group})
    return HttpResponse(html)

def profile(request):
    title='Wearever'
    current_user=request.user
    user=current_user.email
    owm = OWM('47005e466640dd018e9b1e79039f299c')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Stony Brook, US')
    w = observation.weather
    html = render_to_string('profile.html', {'title': title, 'user': user, 'stat': w.detailed_status, 'temp': w.temperature('fahrenheit').get('temp'), 'humid': w.humidity, 'wind': w.wind().get('speed')})
    return HttpResponse(html)
