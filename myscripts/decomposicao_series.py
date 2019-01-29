#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 17:30:07 2019

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
decomposicao = seasonal_decompose(ts)
tendencia = decomposicao.trend
sazonal = decomposicao.seasonal
aleatorio = decomposicao.resid

plt.plot(sazonal)
plt.plot(tendencia)
plt.plot(aleatorio)

plt.subplot(4,1,1)
plt.plot(ts, label="Original")
plt.legend(loc = 'best')

plt.subplot(4,1,2)
plt.plot(tendencia, label="Tendencia")
plt.legend(loc = 'best')

plt.subplot(4,1,3)
plt.plot(sazonal, label="Sazonal")
plt.legend(loc = 'best')

plt.subplot(4,1,4)
plt.plot(aleatorio, label="Aleatorio")
plt.legend(loc = 'best')
plt.tight_layout()