import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline

train = pd.read_csv(r'C:\Users\hrao\Documents\Personal\HK\Python\train.csv')
test = pd.read_csv(r'C:\Users\hrao\Documents\Personal\HK\Python\test.csv')

train.fillna(0)
test.fillna(0)
train = train.drop(['Name','SibSp','Parch','Cabin','Ticket'],axis=1)

print(train.head(n=3))
