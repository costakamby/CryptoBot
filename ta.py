import numpy
import talib
from numpy import genfromtxt

my_data = genfromtxt('historicalETHUSDC.csv',delimiter = ',')
ethusd = my_data[:,4]
timestamp = my_data[:,1]
# close = numpy.random.random(100)

# print(close)


# moving_average = talib.SMA(close,timeperiod=10)
# rsi=talib.RSI(close,14)

# print(moving_average)
# print(rsi)

print(ethusd)

rsi = talib.RSI(ethusd)
print(rsi)

