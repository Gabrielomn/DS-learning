#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 14:19:36 2019

@author: kyouma
"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
from scipy import stats

iris = datasets.load_iris()
stats.describe(iris.data)
previsores = iris.data
classe = iris.target

x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(previsores,
                                                                   classe,
                                                                   test_size = 0.3,
                                                                   random_state = 0)

knn = KNeighborsClassifier(n_neighbors= 3)
knn.fit(x_treinamento, y_treinamento)
previsoes = knn.predict(x_teste)
confusao = confusion_matrix(y_teste, previsoes)
acerto = accuracy_score(y_teste, previsoes)