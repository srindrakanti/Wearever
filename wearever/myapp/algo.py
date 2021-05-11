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

# train_set = []
# train_labels = []
# for i in range(10):
#     a = []
#     t = random.randint(25,45) + random.random()
#     a.append(t)
#     w = random.randint(2,60)
#     a.append(w)
#     h = random.randint(50,99) + random.random()
#     a.append(h)
#     wci = 35.74 + 0.6215*t -  35.75*math.pow(w, 0.16) + 0.4275*t*math.pow(w, 0.16)
#     a.append(wci)
#     train_set.append(a)
#     if i % 2 == 0:
#         train_labels.append([top_list[5], bottom_list[0], footwear_list[0], 2])
#     else:
#         train_labels.append([top_list[5], bottom_list[2], footwear_list[0], 2])

# for i in range(10):
#     a = []
#     T = random.randint(75,100) + random.random()
#     a.append(T)
#     W = random.randint(2,30)
#     a.append(T)
#     RH = random.randint(50,99) + random.random()
#     a.append(RH)
#     hi = -42.379 + 2.04901523*T + 10.14333127*RH - .22475541*T*RH - .00683783*T*T - .05481717*RH*RH + .00122874*T*T*RH + .00085282*T*RH*RH - .00000199*T*T*RH*RH
#     a.append(hi)
#     train_set.append(a)
#     if i % 2 == 0:
#         train_labels.append([top_list[3], bottom_list[2], footwear_list[2], 0])
#     else:
#         train_labels.append([top_list[3], bottom_list[2], footwear_list[1], 0])
# # connect = sqlite3.connect('db.sqlite3')
# # cursor = connect.cursor
# # for row in cursor.execute("SELECT * FROM "):
# #     train_set.append(list(row[:end_ind]))
# #     train_labels.append(list(row[end_ind:]))
# temp = list(zip(train_set, train_labels))
# random.shuffle(temp)
# train_set, train_labels = zip(*temp)
X = [[41.45607499061373, 41, 65.20852262250531], [45.498641651025714, 42, 53.151378937908625], [35.60093452768711, 4, 71.01197054157703], [40.26883198921645, 5, 79.56711706207871], [20.271347970126673, 28, 75.29568736398843], [28.477610460404566, 60, 91.91676211624976], [20.614356969282273, 51, 80.72717323039092], [36.63189791495665, 43, 96.78403106890178], [28.033385832152334, 11, 70.8508986134405], [30.53508004806145, 32, 55.96205171890911], [25.142367019223254, 50, 98.47457610784596], [33.586944034028214, 42, 78.590562797715], 
[32.717455696050735, 17, 87.60769644075626], [15.698501704693934, 5, 84.90567084677966], [42.53289916041263, 33, 73.60843466931463], [83.63203022057043, 9, 85.83386058321454], [87.65268067553706, 3, 50.30223764216016], [97.8507082373719, 2, 87.26301062861451], [97.78839718747619, 15, 54.839430973648064], [85.83341413557753, 17, 83.79601005894499], [100.03089849310034, 7, 68.33996823599061], [96.41315090654032, 14, 82.10847009823287], [81.80134216137893, 12, 68.45107633448305], [99.68751281687784, 15, 61.26113816745326], [80.21665730677198, 9, 70.17498633412887], [79.1933994921324, 11, 57.934287259370926], [79.79507748374354, 8, 62.305323700318844], [87.38413470221508, 8, 83.6696604995595], [92.43436715638248, 21, 73.25926153311559], [79.89536976920077, 16, 64.71283641874426], [48.448204092781644, 12, 55.75425542160728], [69.26290559817431, 11, 61.946820798976105], [52.017410548416585, 14, 63.21950229033305], [69.77425639574378, 20, 83.21041527707492], [59.134405370680284, 28, 77.18267778290694], [53.3804250192221, 27, 61.79735790499898], [52.08057134178162, 11, 61.373271545251534], [66.53584022070875, 3, 87.96464337433575], [67.84309822484336, 14, 61.83194386266636], [75.52458115363227, 3, 80.42222820813568], [69.0940784487185, 10, 91.36874279749162], [61.240847806641824, 9, 56.67374808889327], [52.74435436675365, 25, 68.59331423295293], [64.59230752759224, 18, 98.5654595773951], [64.8214982782411, 4, 71.42763107806655], [70.64986022482957, 26, 61.2775270664432], [49.34657374145485, 4, 50.749036064819606], [73.13447943288463, 25, 60.60215044426277], [62.8129205187668, 4, 99.443643488069], [72.53046315274902, 19, 84.77348359277694], [59.83291961557829, 28, 65.38213362219999], [73.93820175904166, 16, 52.959346534080765], [52.135353861250536, 9, 50.58018352196897], [71.44410011031177, 19, 57.56983162868753], [53.60251002589269, 15, 84.44290346110137], [47.72331455950508, 28, 50.59504221856225], [50.33785417160218, 11, 84.97494260998113], [59.010116387346564, 16, 67.5875416901169], [74.6699990775811, 30, 71.87550098149508], [50.36019159584481, 26, 55.9286792447325]]

y_top = ['wintercoat', 'wintercoat', 'wintercoat', 'wintercoat', 'wintercoat', 'wintercoat', 'wintercoat', 'wintercoat', 'wintercoat', 'wintercoat', 'wintercoat', 'wintercoat', 'wintercoat', 'wintercoat', 'wintercoat', 'tanktop', 'tanktop', 'tanktop', 'tanktop', 'tanktop', 
'tanktop', 'tanktop', 'tanktop', 'tanktop', 'shortsleeve', 'shortsleeve', 'shortsleeve', 'tanktop', 'tanktop', 'shortsleeve', 'sweatshirt', 'longsleeve', 'longsleeve', 'longsleeve', 'longsleeve', 'longsleeve', 'longsleeve', 'longsleeve', 'longsleeve', 'longsleeve', 
'longsleeve', 'longsleeve', 'longsleeve', 'longsleeve', 'longsleeve', 'longsleeve', 'longsleeve', 'longsleeve', 'longsleeve', 'longsleeve', 'longsleeve', 'longsleeve', 'longsleeve', 'longsleeve', 'longsleeve', 'sweatshirt', 'longsleeve', 'longsleeve', 'longsleeve', 
'sweatshirt']

y_bot = ['sweatpants', 'pants', 'pants', 'pants', 'sweatpants', 'sweatpants', 'sweatpants', 'sweatpants', 'sweatpants', 'sweatpants', 'sweatpants', 'sweatpants', 'sweatpants', 'sweatpants', 'pants', 'shorts', 'shorts', 'shorts', 'shorts', 'shorts', 'shorts', 'shorts', 'shorts', 'shorts', 'shorts', 'shorts', 'shorts', 'shorts', 'shorts', 'shorts', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants', 'pants']

y_shoes = ['sneakers', 'sneakers', 'sneakers', 'sneakers', 'boots', 'boots', 'boots', 'sneakers', 'boots', 'boots', 'boots', 'boots', 'sneakers', 'boots', 'sneakers', 'sandals', 'sandals', 'sandals', 'sandals', 'sandals', 'sandals', 'sandals', 'sandals', 'sandals', 'sneakers', 'sneakers', 'sneakers', 'sandals', 'sandals', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers', 'sneakers']

clf_top.fit(X, y_top)
clf_bottom.fit(X, y_bot)
clf_footwear.fit(X, y_shoes)

a = [[37.511, 40, 81.433]]
print(clf_top.predict(a))
print(clf_bottom.predict(a))
print(clf_footwear.predict(a))