from flask import Flask, render_template,request,jsonify
from binance.client import Client
import settings,csv
from decimal import *
getcontext().prec=18

app = Flask(__name__)

client = Client(settings.BINANCE_KEY,settings.BINANCE_SECRET)

@app.route('/')
def index():
    account = client.get_account()
    balances = account['balances']

    exchange_info = client.get_exchange_info()
    
    symbols = exchange_info['symbols']

    return render_template('index.html',balances=balances,symbols=symbols)


@app.route('/buy',methods=['POST'])
def buy():
    print(request.form)
    return 'buy'

@app.route('/sell')
def sell():
    return 'sell'

@app.route('/settings')
def settings():
    return 'settings'

@app.route('/history')
def history():
    candles = client.get_historical_klines(symbol = "ETHBTC",interval = Client.KLINE_INTERVAL_1MINUTE,start_str="1 day ago UTC")
    candlesticks = []

    for candle in candles:
        candlesticks.append({
            "time":int(candle[0])/1000,
            "open":candle[1],
            "high":candle[2],
            "low":candle[3],
            "close":candle[4]
        })


    return jsonify(candlesticks)