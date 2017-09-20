# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 18:45:15 2017

@author: Soulhuntkill
"""
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values


