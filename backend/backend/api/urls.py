from django.urls import path
from .views import index, get_stock_prices

urlpatterns = [
    path('', index, name='index'),
    path('api/get_stocks/', get_stock_prices, name='get_stocks'),
]
