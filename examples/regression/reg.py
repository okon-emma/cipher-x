import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data.csv')
test = pd.read_csv('test.csv')

x_train = df['Father'].values[:,np.newaxis]
y_train = df['Son'].values

x_test = test['Father'].values[:,np.newaxis]

lm =LinearRegression()

###Train the Model
lm.fit(x_train, y_train)
#print(lm)

print("Coefficents: ", end=" ")
print(lm.coef_)
print("MSE: %.2f" % mean_squared_error(x_test, x_train))
print("R Squared: %.2f" % r2_score(x_test, x_train))

###Test the model
#predictions = lm.predict(x_test)
#print(predictions)
