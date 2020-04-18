import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2016,10,10)
end = dt.datetime(2020,4,17)

#df = web.DataReader('CIPLA.NS', 'yahoo', start, end) 
#no = int(input())
#print(df.tail())
#df.to_csv('cipla.csv')

df = pd.read_csv('cipla.csv', parse_dates=True, index_col=0)
df[['Adj Close','Close']].plot()
plt.show()
