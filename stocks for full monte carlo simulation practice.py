import pandas as pd
import yfinance as yf
import pandas_datareader.data as web
from datetime import date
import matplotlib.pyplot as plt
import random



equities_and_value = {"IBM": 600,"MS": 600,"HMC": 600}
simulation_value_list = {}
equities_and_holdings = {"IBM": 33,"MS": 33,"HMC": 33}

simulation_value_list = {}
for k,v in equities_and_value.items():
    simulation_value_list[k]=[v]

def monte_carlo():
    #Simulation set value
    simulations_run_for = 5
    years_run_for = 100
    
    #Initialized variables
    simulation_count = 0
    stock_index = 0
    iterable_stock_list = list(equities_and_holdings)
    
    
    
    #this while loop iterates through every stock in the list
    while(stock_index < len(equities_and_holdings)):
        #select the stock to run simulation on based of while loops iteration
        current_stock = iterable_stock_list[stock_index]
        
        #get price data
        yfticker = yf.Ticker(current_stock)
        stock_info = yfticker.history(period = "max")
        stock_info['year'] = pd.DatetimeIndex(stock_info.index).year
    
        #Clear Dataframe
        clear = ['High','Dividends', 'Stock Splits', 'Open','Low','Volume']
        stock_info.drop(columns = clear, inplace = True)
        
        ### Now that we have the stocks data, lets calculate those percentages
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
        #Thats done! now we need to select a random percentage and add it onto current value however many times we run the simulation for based on the years_run_for
        years_stock_simulation_has_run = 0
        while(years_stock_simulation_has_run < years_run_for):
        # we need to create an equation to compare it to for abnormal gains
            random_number = random.randint(0, len(stock_percent_list) - 1)
            stock_percent_change = (float)(stock_percent_list[random_number])
            #Now we have the percent changes, add it to the previous value
            new_stock_value = (simulation_value_list[current_stock][years_stock_simulation_has_run] * stock_percent_change) + simulation_value_list[current_stock][years_stock_simulation_has_run]
            #Were actually gonna round this cause viewing purposes for now
            new_stock_value = round(new_stock_value, 2)
            simulation_value_list[current_stock].append(new_stock_value)
            #increase for the while loop
            years_stock_simulation_has_run = years_stock_simulation_has_run + 1
            
        stock_index = stock_index + 1
        
        #Were gonna graph a singular simulation here
    plt.subplot(1,2,1)
    graph_iteations_through_stock_list = 0
    #We need to make the years the simulation is run for a list so we can graph it out
    years_run_for_as_a_list = [0]
    years_run_for_as_a_list_number = 0
    while(years_run_for_as_a_list_number < years_run_for):
        years_run_for_as_a_list_number = years_run_for_as_a_list_number  + 1
        years_run_for_as_a_list.append(years_run_for_as_a_list_number)
    #Now we can graph it out
    while(graph_iteations_through_stock_list < len(equities_and_holdings)):
    #list of stocks in list
        graph_stock_list = list(equities_and_holdings)
        graphed_stock = graph_stock_list[graph_iteations_through_stock_list]
        plt.plot(years_run_for_as_a_list, simulation_value_list[graphed_stock], label = graphed_stock)
        graph_iteations_through_stock_list = graph_iteations_through_stock_list + 1
    plt.legend()
    plt.show()
        
monte_carlo()
print(simulation_value_list)

#Alright we need to eliminate outliers again

