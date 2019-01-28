#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 20:57:49 2019

@author: kyouma
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression

base = pd.read_csv('../files/Eleicao.csv', sep = ';')

plt.scatter(base.DESPESAS, base.SITUACAO)
base.describe()

np.corrcoef(base.DESPESAS, base.SITUACAO)

x = base.iloc[:, 2].values
y = base.iloc[:, 1].values
x = x.reshape(-1, 1)
modelo = LogisticRegression()
modelo.fit(x,y)

modelo.score(x,y)

modelo.intercept_
modelo.coef_

test = np.linspace(base.DESPESAS.min(), base.DESPESAS.max(), 100)

def model(x):
    return 1 / (1+np.exp(-x))

r = model(test * modelo.coef_ + modelo.intercept_).ravel()
plt.plot(test, r, color = 'red')

base1 = pd.read_csv('../files/NovosCandidatos.csv', sep = ';')

despesas = base1.iloc[:, 1].values
despesas = despesas.reshape(-1, 1)
modelo.predict(despesas)