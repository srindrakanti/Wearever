import os
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.conf.urls import url

# constants
project_dir = os.getcwd()
title = 'Wearever'

# server
DEBUG = True
SECRET_KEY = '1g3tth053g0053bump53v3ryt1m3'
ROOT_URLCONF = __name__
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            project_dir+"\\templates"
        ],
    },
]

# rendering
def home(request):
    html = render_to_string('home.html', {'title': title})
    return HttpResponse(html)

def about(request):
    group = 'Inverse Intelligence'
    html = render_to_string('about.html', {'title': title, 'group': group})
    return HttpResponse(html)

# routing
urlpatterns = [
    url(r'^$', home, name='homepage'),
    url(r'^about/$', about, name='aboutpage'),
]