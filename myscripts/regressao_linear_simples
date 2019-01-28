#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 16:36:25 2019

@author: kyouma
"""
'''
prevendo a velocidade dos carros a partir da distancia que ele percorreu antes de 
parar
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot
cars = pd.read_csv('../files/cars.csv')

cars = cars.drop(['Unnamed: 0'], axis = 1)
#pegando a variavel independente(no caso, distancia)
x = cars.iloc[:, 1].values 
#pegando a variavel dependente, que sera prevista, que aqui é a velocidade.
y = cars.iloc[:, 0].values
correlacao = np.corrcoef(x,y)
#colocando no formato de array do numpy
x = x.reshape(-1, 1)


modelo = LinearRegression()
modelo.fit(x,y)
'''
 y = ax+b
intercept eh b
modelo.intercept_
coef eh a, o coeficiente linear
modelo.coef_
'''
b = modelo.intercept_
a = modelo.coef_
plt.scatter(x, y)

plt.plot(x, modelo.predict(x), color = 'red')

aPredicaoEhEssaAqui = a*22+b

podeSerAssimTbm = modelo.predict([[22]])

residuos = modelo._residues

