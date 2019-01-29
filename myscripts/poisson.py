#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 16:44:45 2019

@author: kyouma
"""

from scipy.stats import poisson

poisson.pmf(3, 2)
'''
a = 0

numeros = range(4)

for k in numeros:
    
    a += poisson.pmf(k,2)
    
print (a)
mesma coisa que:
'''

poisson.cdf(3,2)

poisson.pmf(12,10)
