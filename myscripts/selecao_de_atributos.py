#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 14:05:43 2019

@author: kyouma
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.svm import SVC
from sklearn.ensemble import ExtraTreesClassifier

credito = pd.read_csv('../files/Credit.csv')
previsores = credito.iloc[:,0:20].values
classe = credito.iloc[:,20].values
previsores[0]

labelencoder = LabelEncoder()
previsores[:,0] = labelencoder.fit_transform(previsores[:,0])
previsores[:,2] = labelencoder.fit_transform(previsores[:,2])
previsores[:,3] = labelencoder.fit_transform(previsores[:,3])
previsores[:,5] = labelencoder.fit_transform(previsores[:,5])
previsores[:,6] = labelencoder.fit_transform(previsores[:,6])
previsores[:,8] = labelencoder.fit_transform(previsores[:,8])
previsores[:,9] = labelencoder.fit_transform(previsores[:,9])
previsores[:,11] = labelencoder.fit_transform(previsores[:,11])
previsores[:,13] = labelencoder.fit_transform(previsores[:,13])
previsores[:,14] = labelencoder.fit_transform(previsores[:,14])
previsores[:,16] = labelencoder.fit_transform(previsores[:,16])
previsores[:,18] = labelencoder.fit_transform(previsores[:,18])
previsores[:,19] = labelencoder.fit_transform(previsores[:,19])

x_treinamento, x_teste, y_treinamento, y_teste = train_test_split(previsores, 
                                                                  classe,
                                                                  test_size = 0.3,
                                                                  random_state = 0 )

svm = SVC()
svm.fit(x_treinamento, y_treinamento)
previsoes = svm.predict(x_teste)
taxa_de_acerto = accuracy_score(y_teste, previsoes)

forest = ExtraTreesClassifier()
forest.fit(x_treinamento, y_treinamento) 
importancias = forest.feature_importances_

x_treinamento2 = x_treinamento[:,[0,1,2,3]]
x_teste2 = x_teste[:,[0,1,2,3]]
svm2 = SVC()
svm2.fit(x_treinamento2, y_treinamento)
previsoes2 = svm2.predict(x_teste2)
taxa_de_acerto2 = accuracy_score(y_teste, previsoes2)