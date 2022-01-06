import pandas as pd
import yfinance as yf
import pandas_datareader.data as web
import datetime

df = web.DataReader('^GSPC', 'yahoo', start='1980-1-1', end='2021-1-1')
df['year'] = pd.DatetimeIndex(df.index).year
clear = ['High','Low','Volume', 'Open', 'Close']
df.drop(columns = clear, inplace = True)
print(df)


val = df.loc[df['year'] == 2020, 'Adj Close'].iloc[0]
print(val)


pct_change_list = []
x = True
date = 1980
while x == True:
    try:
        first = df.loc[df['year'] == date, 'Adj Close'].iloc[0]
        date = date + 1
        second = df.loc[df['year'] == date, 'Adj Close'].iloc[0]
        percent = ((second / first) - 1 ) * 100
        pct_change_list.append(percent)
    except:
        x = False;
    
print(pct_change_list)
print('hi')

