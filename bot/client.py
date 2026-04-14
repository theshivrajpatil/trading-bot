from binance.client import Client
from bot.config import API_KEY, API_SECRET


def get_client():
    client = Client(API_KEY, API_SECRET, testnet=True)

    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    return client