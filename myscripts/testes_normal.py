#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 14:51:53 2019

@author: kyouma
"""

from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt

dados = norm.rvs(size = 100)
stats.probplot(dados, plot = plt)

stats.shapiro(dados)