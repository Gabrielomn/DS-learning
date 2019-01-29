#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 14:35:32 2019

@author: kyouma
"""

from scipy.stats import norm

norm.cdf(6, 8, 2)

norm.sf(6,8,2)

1 - norm.cdf(6,8,2)

(norm.cdf(6,8,2) + (1 - norm.cdf(10,8,2)))