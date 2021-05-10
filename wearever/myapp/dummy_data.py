from myapp.models import Recommendation
import math, random

for i in range(15):
    t = random.randint(25,45) + random.random()
    w = random.randint(2,60)
    h = random.randint(50,99) + random.random()
    wci = 35.74 + 0.6215*t -  35.75*math.pow(w, 0.16) + 0.4275*t*math.pow(w, 0.16)
    print [t,w,h,wci]
