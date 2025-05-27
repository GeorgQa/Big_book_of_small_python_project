import requests

url = "https://api.binance.com/api/v3/ticker/price"
naming_pairs  = ["ETHUSDT", "BTCUSDT", "HYPERBNB","KERNELUSDC" ]

def get_value(params_key):
    place = requests.get(url)
    ticets = place.json()
    for ticet in ticets:
        if ticet["symbol"] in naming_pairs:
            print(f"Цена котировки {ticet['symbol']}: {float(ticet['price'])}")

get_value(naming_pairs)