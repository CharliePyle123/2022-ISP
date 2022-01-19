import pandas as pd
import yfinance as yf
import pandas_datareader.data as web
from datetime import date
import matplotlib.pyplot as plt
import random

#Portfolio equities and percentage holdings
equities_and_holdings = {}
equities_and_holdings_printlist = {}
equities_and_value = {}
simulation_value_list = {}


#USER SHELL INTERFACE
def program():
    #infinite while loop
    forever = 0
    while(forever == 0):
        #Command Print List for User
        print("1: Add a stock to the portfolio")
        print("2: Print out portfolio and percentages")
        print("3: Add more shares or value to a current position, Work In Progress")
        
        #take input from user
        function = (float)(input("Enter a number for a function listed above"))
        
        #Functions
        if(function == 1):
            add_stock()
        if(function == 2):
            portfolio_percentage_conversion()
            print(equities_and_holdings_printlist)

#ASK USER FOR STOCKS

def add_stock():
    #Collect the users stock ticker
    ticker = input("What is your stocks ticker?")
    
    #Date collection and the creation of stock dataframe
    today = date.today()
    current_day = "" + today.strftime("%Y") + "-" + today.strftime("%m") + "-" + today.strftime("%d")
    ticker_data = web.DataReader(ticker, 'yahoo', start=current_day, end=current_day)
     
    
    #ask to input either shares or value and compute the value
    value = 0
    shares_or_value = input("Would you like to input shares or value?")
    if(shares_or_value == "shares"):
        shares = (float)(input("How many shares"))
        value = shares * (float)(ticker_data.iloc[0,3])
    else:
        value = (float)(input("What is the value of your position"))
        
    
    #add the stock and value to the equities and value dictionary
    equities_and_value[ticker] = value
    print(equities_and_value)
    
def portfolio_percentage_conversion():
    
    #get the total of all values and initialize tickers in the equities and holdings list
    list_sum = 0
    length = 0
    for key,val in equities_and_value.items():
        list_sum += val
        length += 1
        equities_and_holdings[key] = 0
        equities_and_holdings_printlist[key] = 0
        
    #Calculate the percentage holdings for each stock and append to equities and holdings
    for key,val in equities_and_value.items():
        percentage = (val / list_sum) * 100
        equities_and_holdings[key] = percentage
        equities_and_holdings_printlist[key] = (str)(percentage) + "%"
    #For indivisual stock loop so we can access value list
    simulation_value_list = {}
    for k,v in equities_and_value.items():
        simulation_value_list[k]=[v]
        
def monte_carlo_portfolio_one_year():
    #get stock from list and make a dataframe
    
    #PUT A WHILE LOOP SO IT CAN ITERATE THROUGH EACH STOCK FOR A YEAR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #index
    iteration = 0
    while(iteration < len(equities_and_holdings)):
    #list of stocks in list
        iterable_stock_list = list(equities_and_holdings)
    
    #WHile LOOP here
    
    #stock on index in list
        stock = iterable_stock_list[iteration]
    
    #get price data
        yfticker = yf.Ticker(stock)
        stock_info = yfticker.history(period = "max")
        stock_info['year'] = pd.DatetimeIndex(stock_info.index).year
    
    #Clear Dataframe
        clear = ['High','Dividends', 'Stock Splits', 'Open','Low','Volume']
        stock_info.drop(columns = clear, inplace = True)
    
    #Percent List Creation
        stock_percent_list = []
        date = stock_info.iloc[0, 1]
        x = True
        while x == True:
            try:
                first = stock_info.loc[stock_info['year'] == date, 'Close'].iloc[0]
                date = date + 1
                second = stock_info.loc[stock_info['year'] == date, 'Close'].iloc[0]
                percent = ((second / first) - 1 )
                stock_percent_list.append(percent)
            except:
                x = False
        
    #Choose a random percent 
        key = random.randint(0, len(stock_percent_list) - 1)
        stock_percent_change = (float)(stock_percent_list[key])
        
        
        #SCAN THIS LOOP FOR INDEX OUT OF RANGE ERROR \\\ the problem is we are appending values to a key and the value is out of range, just keep it a constant for now
        
        new_stock_value = (simulation_value_list[stock][0] * stock_percent_change) + simulation_value_list[stock][0]
    #add it to that specific stocks worth
    
        simulation_value_list[stock].append(new_stock_value)
        iteration = iteration + 1

def carlo_graph():
    #yea
    print()
def monte_carlo_year_iterations():
    run_years;
    while(stock < len(portfolio_and_holdings)):
        monte_carlo_indivisual_stock

program()