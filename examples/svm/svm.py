import numpy as np
from sklearn import svm
from sklearn.datasets import make_circles

df, value = make_circles(n_samples=500, noise=0.05, factor=0.5)
x = df[:,0]
y = df[:,1]
z = x**2 + y**2
test = [[-0.4, -0.4]]

kernals = ['linear', 'poly', 'rbf']
training_set = np.c_[x,y]

for kernal in kernals:
    clf=svm.SVC(kernel=kernal, gamma=2)
    clf.fit(training_set, value)
    prediction = clf.predict(test)
    print(kernal, prediction)
