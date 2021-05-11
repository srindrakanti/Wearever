from sklearn.linear_model import SGDClassifier
import sqlite3
import random
import math

clf_top = SGDClassifier(learning_rate = "optimal", loss="hinge", penalty="l2", max_iter=200)
clf_bottom = SGDClassifier(learning_rate = "optimal", loss="hinge", penalty="l2", max_iter=200)
clf_footwear = SGDClassifier(learning_rate = "optimal", loss="hinge", penalty="l2", max_iter=200)
clf_layers = SGDClassifier(learning_rate = "optimal", loss="hinge", penalty="l2", max_iter=200)

top_list = ["raincoat", "hoodie", "sweatshirt", "short sleeve", "long sleeve", "winter jacket"]
bottom_list = ["pants", "sweatpants", "shorts"]
footwear_list = ["boots", "sneakers", "sandals"]
end_ind = 0

train_set = []
train_labels = []
for i in range(10):
    a = []
    t = random.randint(25,45) + random.random()
    a.append(t)
    w = random.randint(2,60)
    a.append(w)
    h = random.randint(50,99) + random.random()
    a.append(h)
    wci = 35.74 + 0.6215*t -  35.75*math.pow(w, 0.16) + 0.4275*t*math.pow(w, 0.16)
    a.append(wci)
    train_set.append(a)
    if i % 2 == 0:
        train_labels.append([top_list[5], bottom_list[0], footwear_list[0], 2])
    else:
        train_labels.append([top_list[5], bottom_list[2], footwear_list[0], 2])

for i in range(10):
    a = []
    T = random.randint(75,100) + random.random()
    a.append(T)
    W = random.randint(2,30)
    a.append(T)
    RH = random.randint(50,99) + random.random()
    a.append(RH)
    hi = -42.379 + 2.04901523*T + 10.14333127*RH - .22475541*T*RH - .00683783*T*T - .05481717*RH*RH + .00122874*T*T*RH + .00085282*T*RH*RH - .00000199*T*T*RH*RH
    a.append(hi)
    train_set.append(a)
    if i % 2 == 0:
        train_labels.append([top_list[3], bottom_list[2], footwear_list[2], 0])
    else:
        train_labels.append([top_list[3], bottom_list[2], footwear_list[1], 0])
# connect = sqlite3.connect('db.sqlite3')
# cursor = connect.cursor
# for row in cursor.execute("SELECT * FROM "):
#     train_set.append(list(row[:end_ind]))
#     train_labels.append(list(row[end_ind:]))
temp = list(zip(train_set, train_labels))
random.shuffle(temp)
train_set, train_labels = zip(*temp)

print(train_labels[:][0])
clf_top.fit(train_set, train_labels[:][0])
clf_bottom.fit(train_set, train_labels[:][1])
clf_footwear.fit(train_set, train_labels[:][2])
clf_layers.fit(train_set, train_labels[:][3])

a = []
t = random.randint(25,45) + random.random()
a.append(t)
w = random.randint(2,60)
a.append(w)
h = random.randint(50,99) + random.random()
a.append(h)
wci = 35.74 + 0.6215*t -  35.75*math.pow(w, 0.16) + 0.4275*t*math.pow(w, 0.16)
a.append(wci)
print(clf_top.predict(a))
print(clf_bottom.predict(a))
print(clf_footwear.predict(a))
print(clf_layers.predict(a))