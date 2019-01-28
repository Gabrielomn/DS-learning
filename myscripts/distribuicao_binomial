#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 12:10:11 2019

@author: kyouma
"""

import numpy as np
from scipy.stats import binom



probabilidadeDeJogarMoeda5vezesDando3caras = binom.pmf(3,5,0.5)

#passando por 4 sinais de 4 tempos, as probabilidades de passar por 0,1,2,3 e 4
#sinais verdes seguidos.
zero = binom.pmf(0,4,0.25)
uno = binom.pmf(1,4,0.25)
dos = binom.pmf(2,4,0.25)
tres = binom.pmf(3,4,0.25)
quarto = binom.pmf(4,4,0.25)


#e se forem sinais de 2 tempos?

zero2 = binom.pmf(0,4,0.5)
uno2 = binom.pmf(1,4,0.5)
dos2 = binom.pmf(2,4,0.5)
tres2 = binom.pmf(3,4,0.5)
quarto2 = binom.pmf(4,4,0.5)

#concurso com 12 questoes, qual a probabilidade de acertar 7 questões considerando 
#que cada questão tem 4 alternativasssssss?
p = binom.pmf(7, 12, 0.25)
