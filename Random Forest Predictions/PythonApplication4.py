from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

#I'll be using 15 estimators because of what we have established prior

cancerdata = load_breast_cancer()
df = pd.DataFrame(cancerdata['data'], columns=cancerdata['feature_names'])
df['target'] = cancerdata['target']
X = df[cancerdata.feature_names].values
y = df['target'].values
X_train, X_test, y_train, y_test = train_test_split(X, y)
rf = RandomForestClassifier(n_estimators = 15)
rf.fit(X_train, y_train)
acc = rf.score(X_test, y_test)

#Creating random array of features for prediction if the cancer is malignant
a = np.random.random_sample(size=30)
case = a.reshape(1, -1)
pred = rf.predict(case)
print ('Random set of features:')
print (case)
if pred == 0:
    print ('\nPrediction for random set of features is: malignant')
else:
    print('\nPrediction for random set of features is: benign')

#Checking feature importance in prediction

featimp = pd.Series(rf.feature_importances_, index = cancerdata.feature_names).sort_values(ascending = False)
top10 = featimp.head(10)

print ('\nAccuracy:', acc)
print ('\nThe most important values:')
print (top10)