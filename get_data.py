from binance.client import Client
import settings
import csv

client = Client(settings.BINANCE_KEY,settings.BINANCE_SECRET)


# prices = client.get_all_tickers()

# print(prices)

# for price in prices:
#     print(price)#
relevant_symbols = ['BTCUSDC','ALGOUSDC','ETHBTC','ALGOBTC']

for symbol in relevant_symbols:
    candles = client.get_historical_klines(symbol = symbol,interval = Client.KLINE_INTERVAL_1MINUTE, start_str="1 Jan, 2014")

    f= open('historical'+symbol+'.csv','w',newline='')
    candlestick_writer = csv.writer(f,delimiter = ',')

    for candlestick in candles:
        candlestick_writer.writerow(candlestick)
    
    f.close()