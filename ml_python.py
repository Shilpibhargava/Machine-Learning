# -*- coding: utf-8 -*-
"""
Configuring Python environment for machine learning basics
"""
#loading libraries

import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import cross_validation
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#loading the dataset

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length','sepal-width','petal-length','petal-width','class']
dataset = pandas.read_csv(url,names=names)

#shape

print(dataset.shape)

#preview of the dataset

print(dataset.head(20))

#descriptions, statistical summary

print(dataset.describe())

#count(groupby(class))

print(dataset.groupby('class').size())

#univariate plot to understand each of the attributes

dataset.plot(kind='box',subplots=True,layout=(2,2),sharex=False, sharey=False)
plt.show()

#histogram representation of the dataset

dataset.hist()
plt.show()

#multivariate plots

scatter_matrix(dataset)
plt.show()