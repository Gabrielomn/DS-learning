#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 16:59:09 2019

@author: kyouma
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from datetime import datetime

base = pd.read_csv('../files/AirPassengers.csv')
#converte para um tipo data =)
dateparse = lambda dates:pd.datetime.strptime(dates, '%Y-%m')
base = pd.read_csv('../files/AirPassengers.csv', parse_dates =['Month'],
                   index_col = 'Month', date_parser = dateparse)

base.index
#Acessando diferentes datas a partir de diferentes formas =)
ts = base['#Passengers']
oi = base['1949-01']
cu = ts[datetime(1949,2,1)]
ts['1950-01-01':'1950-07-31']
ts[:'1950-07-31']
ts['1950']

ts.index.max()
ts.index.min()

plt.plot(ts)

ts_ano = ts.resample('A').sum()
#ts_year = ts.groupby([lambda x: x.year]).sum() also works

plt.plot(ts_ano)

ts_mes = ts.groupby([lambda x: x.month]).sum()
plt.plot(ts_mes)

ts_datas = ts['1960-01':'1960-12']
plt.plot(ts_datas)