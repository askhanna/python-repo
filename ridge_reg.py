# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.construct import rand

from sklearn.model_selection import RepeatedKFold
from sklearn.linear_model import Ridge
from sklearn.linear_model import RidgeClassifierCV
from sklearn import metrics

#LOAD DATA
url = "https://raw.githubusercontent.com/Statology/Python-Guides/main/mtcars.csv"
data_full = pd.read_csv(url)
data = data_full[["mpg", "wt", "drat", "qsec", "hp"]]

print(data[0:6])

#FIT RIDGE REGRESSION MODEL
#define predictor and response variables
X = data[["mpg", "wt", "drat", "qsec"]]
y = data["hp"]

#define cross-validation method to evaluate model
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)

#define model
model = Ridge()


#fit model
model.fit(X, y)

#display lambda that produced the lowest test MSE
#print(model.alpha_)

#USE MODEL TO PREDICT RESPONSE VALUE OF NEW OBSERVATIONS
#define new observation
new = [18.2, 3.45, 2.85, 22.5]

#predict hp value using ridge regression model
print(model.predict([new]))
