from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf.urls import url
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from django.views.decorators.csrf import csrf_exempt
from myapp.models import Recommendation
from myapp.algo import get_rec

# Create your views here.
def home(request):
    title='Wearever'
    owm = OWM('47005e466640dd018e9b1e79039f299c')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Stony Brook, US')
    w = observation.weather
    #SET DEFAULT RECOMMENDED
    html = render_to_string('home.html', {'title': title, 'stat': w.detailed_status, 'temp': w.temperature('fahrenheit').get('temp'), 'humid': w.humidity, 'wind': round(w.wind('miles_hour').get('speed'),1)})
    return HttpResponse(html)

def about(request):
    group = 'Inverse Intelligence'
    title='Wearever'
    html = render_to_string('about.html', {'title': title, 'group': group})
    return HttpResponse(html)

@csrf_exempt
def profile(request):
    current_user=request.user
    user=current_user.email
    if request.method=='POST':
        top = request.POST['top']
        bottom = request.POST['bottom']
        footwear = request.POST['footwear']
        rec_id = request.POST['rec_id']
        #INPUT INTO DATABASE(IF FEEDBACK ALREADY EXISTS FOR THAT DAY, JUST UPDATE)
        updated_r = Recommendation.objects.get(id=rec_id)
        updated_r.rec = {"top": top, "bottom": bottom, "footwear": footwear}
        updated_r.save()
    title='Wearever'
    owm = OWM('47005e466640dd018e9b1e79039f299c')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Stony Brook, US')
    w = observation.weather
    temp = w.temperature('fahrenheit').get('temp')
    humid = w.humidity
    wind = round(w.wind('miles_hour').get('speed'),1)
    #GET RECOMMENDATIONS FROM MODEL AND PUT INTO HTML
    recs = get_rec(user, temp, humid, wind)
    html = render_to_string('profile.html', {'title': title, 'user': user, 'stat': w.detailed_status, 'temp': temp, 'humid': humid, 'wind': wind,
    'topdefault': recs[1].rec["top"], 'bottomdefault': recs[1].rec["bottom"], 'footweardefault': recs[1].rec["footwear"],
    'rec_id': recs[1].id, 'toprec': recs[0].rec["top"], 'bottomrec': recs[0].rec["bottom"], 'footwearrec': recs[0].rec["footwear"], 'date': recs[1].date})
    return HttpResponse(html)