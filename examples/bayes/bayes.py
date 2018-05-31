import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv('data.csv')

x_train = df.loc[:,'Age':'Nodes']
y_train = df.loc[:,'Survived']
test = [ [12,70,12], [13,20,13] ]

clf = GaussianNB()
clf.fit(x_train, y_train)

prediction = clf.predict(test)
print(prediction)
