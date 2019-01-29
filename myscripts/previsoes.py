#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 17:45:04 2019

@author: kyouma
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from datetime import datetime
from statsmodels.tsa.seasonal import seasonal_decompose

base = pd.read_csv('../files/AirPassengers.csv')
#converte para um tipo data =)
dateparse = lambda dates:pd.datetime.strptime(dates, '%Y-%m')
base = pd.read_csv('../files/AirPassengers.csv', parse_dates =['Month'],
                   index_col = 'Month', date_parser = dateparse)

ts = base['#Passengers']
plt.plot(ts)

ts['1960-01' : '1960-12'].mean()

media_movel = ts.rolling(window = 12).mean()
plt.plot(ts)
plt.plot(media_movel, color = 'blue')

previsoes = []
for i in range(1, 13):
    superior = len(media_movel) - i
    inferior = superior - 11
    previsoes.append(media_movel[inferior:superior].mean())
    
previsoes = previsoes[::-1]
plt.plot(previsoes)