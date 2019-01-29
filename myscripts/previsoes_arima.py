#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 18:07:01 2019

@author: kyouma
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from datetime import datetime
from statsmodels.tsa.arima_model import ARIMA
from pmdarima.arima import auto_arima

base = pd.read_csv('../files/AirPassengers.csv')
#converte para um tipo data =)
dateparse = lambda dates:pd.datetime.strptime(dates, '%Y-%m')
base = pd.read_csv('../files/AirPassengers.csv', parse_dates =['Month'],
                   index_col = 'Month', date_parser = dateparse)

ts = base['#Passengers']

modelo = ARIMA(ts, order=(2,1,2))
modelo_treinado = modelo.fit()

modelo_treinado.summary()

previsoes = modelo_treinado.forecast(steps = 12)[0]

eixo = ts.plot()

#modelo_treinado.plot_predict('1960-01','1962-01') interessante tbm =), apenas o ano anterior e a previsao
#observe que se usado um intervalo muito grande a previsao vira uma linha
modelo_treinado.plot_predict('1960-01','1962-01', ax = eixo, plot_insample = True)

modelo_auto = auto_arima(ts, m = 12, seasonal = True, trace = True)