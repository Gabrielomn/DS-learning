#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 17:39:07 2019

@author: kyouma
"""
import numpy as np
from scipy.stats import chi2_contingency

novela = np.array([[19, 6], [43, 32]])

chi2_contingency(novela)

a = 0
for i in range(20):
    a+= i
    
print (a)