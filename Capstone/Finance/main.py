# from datetime import datetime
# import pandas_datareader.data as web
#
# # Bank of America
# BAC = web.DataReader("BAC", 'av-daily', start= datetime(2006, 1, 1), end= datetime(2016, 1, 1), api_key="M5HX0YCPSMIZQWCM")
# # Goldman Sachs
# GS = web.DataReader("GS", 'av-daily', start= datetime(2006, 1, 1), end= datetime(2016, 1, 1), api_key="M5HX0YCPSMIZQWCM")
# # JPMorgan Chase
# JPM = web.DataReader("JPM", 'av-daily', start= datetime(2006, 1, 1), end= datetime(2016, 1, 1), api_key="M5HX0YCPSMIZQWCM")
# # Morgan Stanley
# MS = web.DataReader("MC", 'av-daily', start= datetime(2006, 1, 1), end= datetime(2016, 1, 1), api_key="M5HX0YCPSMIZQWCM")
# # Wells Fargo
# WFC = web.DataReader("WFC", 'av-daily', start= datetime(2006, 1, 1), end= datetime(2016, 1, 1), api_key="M5HX0YCPSMIZQWCM")

# # need a premium account to retrieve information directly from the web


#importing packages
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as mpl
import numpy as np
import datetime

#reading the file
bank_stocks = pd.read_pickle('all_banks')
print(bank_stocks.head())

#printing the max close price for each bank
print(bank_stocks.xs(key='Close',axis=1,level='Stock Info').max())

#creating a new dataframe
returns = pd.DataFrame()

#adding columns to the new dataframe that contain the returns for each bank
tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']
for tick in tickers:
    returns[tick+' Return'] = bank_stocks[tick]['Close'].pct_change()
print(returns.head())

#plotting a pair plot on returns
sns.pairplot(returns)
mpl.show()

#printing the day with the least drop in retruns for each bank
print(returns.idxmin())

#printing the day with the least drop in retruns for each bank
print(returns.idxmax())

#printing the standard deviation in retruns for each bank
print(returns.std())

#printing the standard deviation though the year 2015 in retruns for each bank
print(returns.loc['2015-01-01':'2015-12-31'].std())

#plotting a histogram for the returns of morgan stanley in 2015
sns.distplot(returns.loc['2015-01-01':'2015-12-31']['MS Return'])
mpl.show()

#plotting a histogram for the returns of citigroup in 2008
sns.distplot(returns.loc['2008-01-01':'2008-12-31']['C Return'])
mpl.show()

#plotting a line plot for the close price for each bank
bank_stocks.xs(key='Close',axis=1,level='Stock Info').plot.line()
mpl.show()

#plotting the rolling 30 day average against the Close Price for Bank Of America's stock for the year 2008
bank_stocks["BAC"]['Close'].loc['2008-01-01':'2009-01-01'].rolling(window=30).mean().plot(label='30 Day Avg') 
bank_stocks["BAC"]['Close'].loc['2008-01-01':'2009-01-01'].plot(label='BAC CLOSE')
mpl.legend()
mpl.show()

#creating a correlation of the close price for each bank and then plotting a heat map
sns.heatmap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)
mpl.show()

#creating a correlation of the close price for each bank and then plotting a cluster map
sns.clustermap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)
mpl.show()









