import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('data.csv')

x_train = df.loc[:,'buying':'safety']
y_train = df.loc[:,'values']
test = [[4,3,2,1,2,3]]

tree = DecisionTreeClassifier(max_leaf_nodes=3, random_state=0)
tree.fit(x_train, y_train)

prediction = tree.predict(test)
print(prediction)
