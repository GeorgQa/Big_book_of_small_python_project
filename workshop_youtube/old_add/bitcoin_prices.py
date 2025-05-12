import requests
import time

url = "https://api.binance.com/api/v3/ticker/price"

bitcoin_prices = []
for i in range(30):
    prise_response = requests.get(url, params={'symbol': 'BTCUSDT'})
    prise_object = float(prise_response.json()['price'])
    bitcoin_prices.append(prise_object)
    time.sleep(1)

print(bitcoin_prices)
print(len(bitcoin_prices))
print(max(f"Максимальное значение из списка {bitcoin_prices}"))
print(min(f"Минимальное значение из списка {bitcoin_prices}"))