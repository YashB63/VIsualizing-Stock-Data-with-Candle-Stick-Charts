import datetime as dt
import pandas_datareader as pdr
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates
from mpl_finance import candlestick_ohlc#open high low close

#define Time Frame

start = dt.datetime(2023,5,1) #year,month,day
end = dt.datetime.now()

#Load Data

ticker = 'AAPL'
df = pdr.DataReader(ticker,'yahoo',start,end)
#print(df.columns)

#Restructure Data

df = df[['Open', 'High', 'Low', 'Close']]

df.reset_index(inplace=True)
df['Date'] = df['Date'].map(mdates.date2num)

#print(df.head())

#Visualization

ax = plt.subplot()
ax.grid(True)
ax.set_axisbelow(True)
ax.set_title('() Share Price'.format(ticker) , color='White')
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')#dark grey
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.xaxis_date()

candlestick_ohlc(ax, df.values, width=0.5, colour='g')
plt.show()