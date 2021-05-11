from sklearn.linear_model import SGDClassifier
import sqlite3

clf_top = SGDClassifier(loss="hinge", penalty="l2", max_iter=200)
clf_bottom = SGDClassifier(loss="hinge", penalty="l2", max_iter=200)
clf_footwear = SGDClassifier(loss="hinge", penalty="l2", max_iter=200)
clf_layers = SGDClassifier(loss="hinge", penalty="l2", max_iter=200)

top_list = ["raincoat", "hoodie", "sweatshirt", "short sleeve", "long sleeve", "winter jacket"]
bottom_list = ["pants", "sweatpants", "shorts"]
footwear_list = ["boots", "sneakers", "sandals"]
end_ind = 0

train_set = []
train_labels = []
connect = sqlite3.connect('db.sqlite3')
cursor = connect.cursor
for row in cursor.execute("SELECT * FROM "):
    train_set.append(list(row[:end_ind]))
    train_labels.append(list(row[end_ind:]))

clf_top.fit(train_set, train_labels[:][0])
clf_bottom.fit(train_set, train_labels[:][1])
clf_top.fit(train_set, train_labels[:][2])
clf_bottom.fit(train_set, train_labels[:][3])

