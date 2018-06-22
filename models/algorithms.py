import numpy as np
from sklearn import linear_model, datasets
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split
from numpy import array
import pandas as pd

df = pd.read_csv('train.csv')
X = df.loc[:,'r3':'odd']
y = df.loc[:,'class']

X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, test_size=0.2, random_state=15)

h = 0.02 ##step size in the mesh
logreg = linear_model.LogisticRegression(C=1e5)
logreg.fit(X_train, y_train)
score_logit = logreg.score(X_test, y_test)
print("------------------")
print("Logit Model Accuracy: %.2f%%" % (score_logit*100))

clf = GaussianNB()
clf.fit(X_train, y_train)
score_gaussian = clf.score(X_test, y_test)
print("------------------")
print("Bayes Gaussian Model Accuracy: %.2f%%" % (score_gaussian*100))

tree = DecisionTreeClassifier(max_leaf_nodes=3, random_state=0)
tree.fit(X_train, y_train)
score_tree = tree.score(X_test, y_test)
print("------------------")
print("Decision Tree Model Accuracy: %.2f%%" % (score_tree*100))

kernals = ['linear', 'rbf']
for kernal in kernals:
    clf=svm.SVC(kernel=kernal, gamma=2)
    clf.fit(X_train, y_train)
    score_svm = clf.score(X_test, y_test)
    print("------------------")
    print("SVM " + kernal + "Model Accuracy:" + " %.2f%%" % (score_svm*100))
