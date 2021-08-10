# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.construct import rand

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# load data
url = "https://raw.githubusercontent.com/Statology/Python-Guides/main/default.csv"
data=pd.read_csv(url)

# view first 6 rows
print(data.head(6))

print("Total number of observations: ", data.shape[0])

# fit logistic regression model
X = data[['student','balance','income']]
y = data['default']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)

clf = LogisticRegression()
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)

#MODEL DIAGNOSTICS
cnf_matrix = metrics.confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cnf_matrix)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

# plot ROC curve
y_pred_proba = clf.predict_proba(X_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.plot(fpr,tpr,label="AUC="+str(auc))
plt.legend(loc=4)
plt.show()
