from sklearn.datasets import load_breast_cancer
import pandas as pd
#Here I'd like to have a way to look into the dataset and access information that may be concidered crucial later e.g. in interpretation 

cancerdata = load_breast_cancer()
df = pd.DataFrame(cancerdata['data'], columns=cancerdata['feature_names'])
df['target'] = cancerdata['target']
#0 = malignant, 1 = benign
print (df.info())
print (df.head(10))