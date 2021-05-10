from sklearn.linear_model import SGDClassifier

X = [[0., 0.], [1., 1.]]
y = [0, 1]
clf = SGDClassifier(loss="hinge", penalty="l2", max_iter=200)
print(clf.fit(X, y))
