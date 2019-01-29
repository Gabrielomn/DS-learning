#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 19:43:18 2019

@author: kyouma
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm

base = pd.read_csv('../files/mt_cars.csv')
base = base.drop(['Unnamed: 0'], axis = 1)

cilindradas = base.iloc[:, 2].values
consumo = base.iloc[:, 0].values 
corr = np.corrcoef(consumo, cilindradas)

cilindradas = cilindradas.reshape(-1, 1)

modelo = LinearRegression()
modelo.fit(X = cilindradas, y = consumo)

modelo.coef_
modelo.intercept_
plt.scatter(cilindradas, consumo)
plt.plot(cilindradas, modelo.predict(cilindradas), color = 'red')

modelo.score(cilindradas, consumo) #r2 normal
predicao = modelo.predict(cilindradas)
modelo_ajustado = sm.ols(formula = 'mpg ~ disp', data = base) #r2 ajustado
modelo_treinado = modelo_ajustado.fit()

modelo_treinado.summary()

modelo.predict([[200]])
#fazendo a regressao linear a partir de multiplos valores agora
variaveis_independentes = base.iloc[:, 1:4].values
#newcorr = np.corrcoef(variaveis_independentes, consumo)
modelo2 = LinearRegression()
modelo2.fit(variaveis_independentes, consumo)
modelo2.score(variaveis_independentes, consumo)

#verificando o r2 ajustado quando se leva em consideração as variaveis que sao agora
#usadas como variaveis independentes
modelo_ajustado2 = sm.ols(formula = 'mpg ~ cyl + disp + hp', data = base) 
modelo_treinado2 = modelo_ajustado2.fit()
modelo_treinado2.summary()

novo = np.array([4, 200, 100])
novo = novo.reshape(1, -1)
modelo2.predict(novo)