# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 02:09:03 2022

@author: Ashutosh
"""
'''Decomposing a Time Series into Its Components'''


#Decomposition is a method used to isolate the time-series data into different elements such as trends, seasonality, cyclic variance, and residuals. We can leverage seasonal decomposition from a stats model to decompose the data into its constituent parts, considering series as additive or multiplicative.
#Trends(T(t)) means an increase or decrease in the value of ts data.

#Seasonality(S[t]) means repeating a short-term cycle of ts data.

#Cyclic variations(c[t]) means a fluctuation in long trends of ts data.

#Residuals(e[t]) means an irregular variation of ts data.


from statsmodels.tsa.seasonal import seasonal_decompose
import pandas as pd
df = pd.read_excel(r'Data\India_Exchange_Rate_Dataset.xls',
index_col=0,parse_dates=True)
result = seasonal_decompose(df['EXINUS'], model='add')
result.plot()
result = seasonal_decompose(df['EXINUS'], model='mul')
result.plot()




