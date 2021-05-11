from .models import Recommendation
import math, random


#winter
for i in range(10):
    t = random.randint(25,45) + random.random()
    w = random.randint(2,60)
    h = random.randint(50,99) + random.random()
    wci = 35.74 + 0.6215*t -  35.75*math.pow(w, 0.16) + 0.4275*t*math.pow(w, 0.16)
    print [t,w,h,wci]

#summer
for i in range(10):
    T = random.randint(75,100) + random.random()
    w = random.randint(2,30)
    RH = random.randint(50,99) + random.random()
    hi = -42.379 + 2.04901523*T + 10.14333127*RH - .22475541*T*RH - .00683783*T*T - .05481717*RH*RH + .00122874*T*T*RH + .00085282*T*RH*RH - .00000199*T*T*RH*RH
    print [T,w,RH,hi]
