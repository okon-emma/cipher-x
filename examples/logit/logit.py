import numpy as np
from sklearn import linear_model, datasets
from numpy import array
import pandas as pd

df = pd.read_csv('data.csv')
x_train = df.loc[:,'Age':'Nodes']
y_train = df.loc[:,'Survived']
test = [ [12,70,12], [13,20,13] ]

h = 0.02 ##step size in the mesh

logreg = linear_model.LogisticRegression(C=1e5)
logreg.fit(x_train,y_train)

###Test the model
predictions = logreg.predict(test)
print(predictions)
