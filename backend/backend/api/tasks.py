from celery import shared_task
import requests
import redis
import datetime

URL = 'https://www.alphavantage.co/query'
API_KEY = 'QQHENYSQOQ3GHMSA'


@shared_task
def fetch_stock_price(symbol):
    url = URL
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()
    price = data['Global Quote']['05. price']
    curr_time = datetime.datetime.now()
    timestamp = curr_time.strftime("%Y-%m-%d %H:%M:%S")
    redis_client = redis.Redis(host='localhost', port=6379)
    redis_client.lpush(f"{symbol}_prices", price)
    redis_client.lpush(f"{symbol}_timestamps", timestamp)
    redis_client.ltrim(f"{symbol}_prices", 0, 9)
    redis_client.ltrim(f"{symbol}_timestamps", 0, 9)


@shared_task
def fetch_crypto_price(symbol):
    url = URL
    params = {
        'function': 'CURRENCY_EXCHANGE_RATE',
        'from_currency': symbol,
        'to_currency': 'PLN',
        'apikey': API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()
    price = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    curr_time = datetime.datetime.now()
    timestamp = curr_time.strftime("%Y-%m-%d %H:%M:%S")
    redis_client = redis.Redis(host='localhost', port=6379)
    redis_client.lpush(f"{symbol}_prices", price)
    redis_client.lpush(f"{symbol}_timestamps", timestamp)
    redis_client.ltrim(f"{symbol}_prices", 0, 9)
    redis_client.ltrim(f"{symbol}_timestamps", 0, 9)
