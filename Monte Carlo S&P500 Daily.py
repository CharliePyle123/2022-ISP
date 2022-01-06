import pandas as pd
import yfinance as yf
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import random

#Creating pandas dataframe of close prices for every day and year of the S&P500
df = web.DataReader('^GSPC', 'yahoo', start='1970-1-1', end='2022-1-1')
df['year'] = pd.DatetimeIndex(df.index).year


clear = ['High','Low','Volume', 'Open', 'Close']
df.drop(columns = clear, inplace = True)
val = df.loc[df['year'] == 2020, 'Adj Close'].iloc[0]


#list of yearly SAP gains
pct_change_list = []
x = True
row = 0
while x == True:
    try:
        first = df.iat[row, 0]
        row = row + 1
        second = df.iat[row, 0]
        percent = ((second / first) - 1 )
        pct_change_list.append(percent)
    except:
        x = False;
#print(pct_change_list)

possible_outcomes = []
def random_path():
    #to be set by user
    portfolio_value = 80000
    year = 2022
    years_untill_retirement = 30
    day = 0
    days_untill_retirement = years_untill_retirement * 365
    
    #for graph 
    days = [day]
    yearly_gains = [0]
    portfolio_value_list = [portfolio_value]
    
    #run simulation
    while day <= days_untill_retirement:
        day_of_week = 0
        if(day_of_week < 5):
            key = random.randint(0, len(pct_change_list) - 1)
            change = (float)(pct_change_list[key])
            portfolio_value = ((change * portfolio_value) + portfolio_value)
            portfolio_value_list.append(portfolio_value)
            day = day + 1
            day_of_week = day_of_week + 1
            days.append(day)
        else:
            if(day_of_week < 7):
                change = (float)(0)
                portfolio_value = ((change * portfolio_value) + portfolio_value)
                portfolio_value_list.append(portfolio_value)
                day = day + 1
                day_of_week = day_of_week + 1
                days.append(day)
            else:
                day_of_week = 0
                
                
    
    
    plt.plot(days, portfolio_value_list)
    
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
    
monte_carlo(500)
#eliminate outliers


#print out everything

print(possible_outcomes)   
average = sum(possible_outcomes) / len(possible_outcomes)
print(average)
plt.show()





