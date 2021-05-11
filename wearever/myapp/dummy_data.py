import math, random

top = ["wintercoat","sweatshirt", "longsleeve", "shortsleeve", "tanktop"]
bottom = ["sweatpants", "pants", "shorts"]
footwear = ["boots", "sneakers", "sandals"]
x = []
yt = []
yb = []
yf = []
#winter
for i in range(15):
    t = random.randint(15,45) + random.random()
    w = random.randint(2,60)
    h = random.randint(50,99) + random.random()
    wci = 35.74 + 0.6215*t -  35.75*math.pow(w, 0.16) + 0.4275*t*math.pow(w, 0.16)

    if wci<20:
        yt.append("wintercoat")
        yb.append("sweatpants")
        yf.append("boots")

    elif 20<wci<30:
        yt.append("wintercoat")
        yb.append("sweatpants")
        yf.append("sneakers")
    elif 30<wci:
        yt.append("wintercoat")
        yb.append("pants")
        yf.append("sneakers")
    x.append([t,w,h])


#summer
for i in range(15):
    t = random.randint(75,100) + random.random()
    w = random.randint(2,30)
    h = random.randint(50,99) + random.random()
    hi = -42.379 + 2.04901523*t + 10.14333127*h - .22475541*t*h - .00683783*t*t - .05481717*h*h + .00122874*t*t*h + .00085282*t*h*h - .00000199*t*t*h*h
    
    if t<80:
        yt.append("shortsleeve")
        yb.append("shorts")
        yf.append("sneakers")

    elif 70<hi<85:
        yt.append("shortsleeve")
        yb.append("shorts")
        yf.append("sneakers")
    elif 85<hi:
        yt.append("tanktop")
        yb.append("shorts")
        yf.append("sandals")
    x.append([t,w,h])

#spring/fall
for i in range(30):
    t = random.randint(45,75) + random.random()
    w = random.randint(2,30)
    h = random.randint(50,99) + random.random()
    wci = 35.74 + 0.6215*t -  35.75*math.pow(w, 0.16) + 0.4275*t*math.pow(w, 0.16)
    
    if wci<45:
        yt.append("sweatshirt")
        yb.append("pants")
        yf.append("sneakers")

    elif 45<wci<65:
        yt.append("longsleeve")
        yb.append("pants")
        yf.append("sneakers")
    elif 65<wci:
        yt.append("longsleeve")
        yb.append("pants")
        yf.append("sneakers")
    x.append([t,w,h])

print(x)
print(yt)
print(yb)
print(yf)