#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 19:59:48 2019

@author: kyouma
"""

import pandas as pd
import numpy as np
import math

populacao = 150
amostra = 15

k = math.ceil(populacao/amostra)

    
rand = np.random.randint(low = 1, high = k+1, size = 1)
acumulador = rand[0]

sorteados = []

for i in range(amostra):
    sorteados.append(acumulador + (i*k))
    
base = pd.read_csv('../files/iris.csv')
base_sorteados = base.loc[sorteados]