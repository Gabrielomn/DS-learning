#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 19:01:48 2019

@author: kyouma
"""

from sklearn import datasets
from sklearn.metrics import confusion_matrix
import numpy as np
from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster import cluster_visualizer

iris = datasets.load_iris()

cluster = kmedoids(iris.data[:,0:2], [3,12,20])
cluster.process()
previsoes = cluster.get_clusters()
medoides = cluster.get_medoids()

v = cluster_visualizer()
v.append_clusters(previsoes, iris.data[:, 0:2])
v.append_cluster(medoides, data = iris.data[:, 0:2], marker = "^", markersize = 15)
v.show()

lista_previsoes = []
lista_real = []

for e in previsoes:
    lista_previsoes.append(e)
    for k in e:
        lista_real.append(iris.target[k])