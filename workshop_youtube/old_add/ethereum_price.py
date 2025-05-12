import requests

price = requests.get("https://api.binance.com/api/v3/ticker/price")
ethereum = price.json()

for ticker in price.json():
    if ticker['symbol'] == 'ETHUSDT':
        print(float(ticker['price']))