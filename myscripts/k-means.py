#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 17:27:24 2019

@author: kyouma
"""

from sklearn import datasets
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

iris = datasets.load_iris()
previsores = iris.data
unicos, quantidades = np.unique(iris.target, return_counts = True)

cluster = KMeans(n_clusters = 3)
cluster.fit(previsores)

centroides = cluster.cluster_centers_
previsoes = cluster.labels_

unicos2, quantidade2 = np.unique(previsoes, return_counts = True)
resultados = confusion_matrix(iris.target, previsoes)

plt.scatter(iris.data[previsoes == 0, 0], iris.data[previsoes == 0, 1], c = 'green', label = 'setosa')
plt.scatter(iris.data[previsoes == 1, 0], iris.data[previsoes == 1, 1], c = 'red', label = 'veersicolor')
plt.scatter(iris.data[previsoes == 2, 0], iris.data[previsoes == 2, 1], c = 'blue', label = 'virginica')

