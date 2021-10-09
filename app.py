from flask import Flask, render_template,request
from binance.client import Client
import settings,csv

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

