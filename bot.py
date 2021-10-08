import ccxt
import settings

exchange = ccxt.coinbasepro({
    'apiKey': settings.COINBASE_PRO_KEY,
    'secret': settings.COINBASE_PRO_SECRET,
    'password': settings.COINBASE_PRO_PASSWORD
})

print(exchange)

markets = exchange.load_markets()

symbol = "ETH/USD"
ticker=exchange.fetch_ticker(symbol)



balance = exchange.fetch_balance()

print(balance['total']['GBP'])

print(balance['total']['ETH'])
