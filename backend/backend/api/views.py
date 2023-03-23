from django.shortcuts import  redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
import redis


def index(request):
    return redirect('http://localhost:3000/')


@api_view(['GET'])
def get_stock_prices(request):
    redis_client = redis.Redis(host='localhost', port=6379)
    symbols = ['AAPL', 'INTC', 'NVDA', 'BTC', 'ETH']
    stocks = []
    for symbol in symbols:
        prices = redis_client.lrange(f"{symbol}_prices", 0, 9)[::-1]
        timestamps = redis_client.lrange(f"{symbol}_timestamps", 0, 9)[::-1]
        stocks.append({'name': symbol,
                     'date': timestamps,
                     'price': prices})
    return Response(stocks)
