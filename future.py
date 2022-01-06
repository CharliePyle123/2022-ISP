import pandas as pd
import yfinance as yf
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import random

#Creating pandas dataframe of close prices for every day and year of the S&P500
df = web.DataReader('^GSPC', 'yahoo', start='1980-1-1', end='2021-1-1')
df['year'] = pd.DatetimeIndex(df.index).year
clear = ['High','Low','Volume', 'Open', 'Close']
df.drop(columns = clear, inplace = True)
val = df.loc[df['year'] == 2020, 'Adj Close'].iloc[0]


#list of yearly SAP gains
pct_change_list = []
x = True
date = 1980
while x == True:
    try:
        first = df.loc[df['year'] == date, 'Adj Close'].iloc[0]
        date = date + 1
        second = df.loc[df['year'] == date, 'Adj Close'].iloc[0]
        percent = ((second / first) - 1 )
        pct_change_list.append(percent)
    except:
        x = False;
#print(pct_change_list)

possible_outcomes = []
def random_path():
    #to be set by user
    portfolio_value = 80000
    year = 2021
    years_untill_retirement = 30
    
    #for graph 
    years = [year]
    yearly_gains = [0]
    portfolio_value_list = [portfolio_value]
    
    #run simulation
    v = 0
    while v <= years_untill_retirement:
        key = random.randint(0, len(pct_change_list) - 1)
        change = (float)(pct_change_list[key])
        portfolio_value = ((change * portfolio_value) + portfolio_value)
        portfolio_value_list.append(portfolio_value)
        year = year + 1
        years.append(year)
        v = v + 1
    
    plt.plot(years, portfolio_value_list)
    
    #to average out outcomes
    final_outcome = portfolio_value_list[len(portfolio_value_list) - 1]
    possible_outcomes.append(final_outcome)
    

def monte_carlo(sims):
    total_sims = 0
    sim_limit = sims
    while total_sims < sim_limit:
        random_path()
        total_sims = total_sims + 1
    #plt.show()
    
monte_carlo(50)
print(possible_outcomes)   
average = sum(possible_outcomes) / len(possible_outcomes)
print(average)
plt.show()
    




