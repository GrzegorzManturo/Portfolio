from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import pandas as pd
import matplotlib.pyplot as plt

cancerdata = load_breast_cancer()
df = pd.DataFrame(cancerdata['data'], columns=cancerdata['feature_names'])
df['target'] = cancerdata['target']
X = df[cancerdata.feature_names].values
y = df['target'].values
n_estimators = list(range(1,101))
param_grid = {
    'n_estimators' : n_estimators
    }
rf = RandomForestClassifier()
gs = GridSearchCV(rf, param_grid, cv=5)
#I'm using gridsearch metod to find the best performing number of estimators.
#I'm also portraiting it on an elbow graph to see where the graph levels out
# to make sure I'm picking best compromise between performance and computation consumption.
gs.fit(X,y)
score = gs.cv_results_['mean_test_score']
plt.plot(n_estimators, score)
plt.xlim(0, 100)
plt.ylim(0.9, 1)
plt.xlabel('Number of trees')
plt.ylabel('Score')
plt.show()
#As it  turns out the best n_estimators parameter is somewhere between 15 and 20. It differs because of randomization process.
#You can see that in attachet jpeg of said graph
