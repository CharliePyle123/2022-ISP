import pandas as pd
import yfinance as yf
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import random

#Creating pandas dataframe of close prices for every day and year of the S&P500
df = web.DataReader('^GSPC', 'yahoo', start='1970-1-1', end='2021-1-1')
df['year'] = pd.DatetimeIndex(df.index).year
clear = ['High','Low','Volume', 'Open', 'Close']
df.drop(columns = clear, inplace = True)
val = df.loc[df['year'] == 2020, 'Adj Close'].iloc[0]
print(df)

row = 1
print(df.iat[row, 0])