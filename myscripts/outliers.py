#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 19:29:36 2019

@author: kyouma
"""

import matplotlib.pyplot as plt
import pandas as pd
from pyod.models.knn import KNN

iris = pd.read_csv('../files/iris.csv')

#para n mostrar os outliers basta: plt.boxplot(iris.iloc[:,1], showfliers = True)
plt.boxplot(iris.iloc[:,1])
outliers = iris[(iris['sepal width'] > 4) | (iris['sepal width'] < 2.1)]
sepal_width = iris.iloc[:,1].values
sepal_width = sepal_width.reshape(-1,1)
detector = KNN()
detector.fit(sepal_width)
previsoes = detector.labels_

