# -*- coding: utf-8 -*-
import pandas as pd

import numpy as np

base = pd.read_csv('../files/iris.csv')
np.random.seed(124)
amostra = np.random.choice(range(150), size = 20)
amostragem = pd.DataFrame()

for i in range(20):
    amostragem = amostragem.append(base.loc[amostra[i]])

amostragem.index = range(20)