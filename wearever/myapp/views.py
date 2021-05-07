from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf.urls import url

# Create your views here.
def home(request):
    title='Wearever'
    html = render_to_string('home.html', {'title': 'Wearever'})
    return HttpResponse(html)

def about(request):
    group = 'Inverse Intelligence'
    title='Wearever'
    html = render_to_string('about.html', {'title': title, 'group': group})
    return HttpResponse(html)


