# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 23:24:31 2019

@author: Dell
"""


'''

The EMA is similar to the simple moving average, but, instead of weighing all prices in the
history equally, it places more weight on the most recent price observation and less weight
on the older price observations. This is endeavoring to capture the intuitive idea that the
new price observation has more up-to-date information than prices in the past. It is also
possible to place more weight on older price observations and less weight on the newer
price observations. This would try to capture the idea that longer-term trends have more
information than short-term volatile price movements.

The weighting depends on the selected time period of the EMA; the shorter the time period,
the more reactive the EMA is to new price observations; in other words, the EMA
converges to new price observations faster and forgets older observations faster, also
referred to as Fast EMA. The longer the time period, the less reactive the EMA is to new
price observations; that is, EMA converges to new price observations slower and forgets
older observations slower, also referred to as Slow EMA.
Based on the description of EMA, it is formulated as a weight factor, , applied to new price
observations and a weight factor applied to the current value of EMA to get the new value
of EMA.

'''

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

n=20 #where n is the time period as described
smoothingConstant=2/(n+1)
EMAprice=0
EMAvalues=[]

#download data
data=yf.download('GOOG',start='2015-9-1',end='2018-11-11')
adjustedClose=data['Adj Close']

#declaring variables and finding mean
for price in adjustedClose:
    if EMAprice==0:
        EMAprice=price
    else:
        EMAprice=(price-EMAprice)*smoothingConstant+EMAprice
    EMAvalues.append(EMAprice)
    
closePrice=pd.DataFrame(adjustedClose,index=data.index)
closePrice['20dayEMA']=EMAvalues
closePrice['adjustedPrice']=adjustedClose

plotClosePrice=closePrice['adjustedPrice']
plot20dayEMA=closePrice['20dayEMA'] 

#visualise code
fig=plt.figure()
axis=fig.add_subplot(111,ylabel='Plot of google stocks exponential moving average')
plotClosePrice.plot(ax=axis, color='g', lw=2., legend=True)
plot20dayEMA.plot(ax=axis, color='b', lw=2., legend=True)
plt.show()

     
        