import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('data.csv')

x_train = df.loc[:,'sepal_length':'petal_width']
y_train = df.loc[:,'class']
test = [[4.9,7.0,1.2,0.2]]

knn = KNeighborsClassifier()
knn.fit(x_train, y_train)

prediction = knn.predict(test)
print(prediction)
