import json, requests
from models.assets.Stock import Stock

class MarketProvider:

    # GLOBALS
    API_TOKEN = ""  # NEVER EVER COMMIT THIS
    API_URL = "https://sandbox.tradier.com/v1"     # If you change the API you have to update the objects dumped to

    HEADERS = {"Authorization": "Bearer "+API_TOKEN, "Accept": "application/json"}

    @classmethod
    def getStock(cls, symbol: str):
        response = requests.get(cls.API_URL + "/markets/quotes?symbols=" + symbol,
        params={"greeks": "false"},
        headers=cls.HEADERS)
        
        stockJson = response.json()
        return Stock.from_json(stockJson)

    @classmethod
    def getHistoricalData(cls, symbol: str):
        response = requests.get(cls.API_URL + "/markets/history?symbols=" + symbol,
        params={"start": "2000-01-01"},
        headers=cls.HEADERS)

        return response.json()
