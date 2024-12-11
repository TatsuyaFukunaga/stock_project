from django.urls import path
from .views import get_stock_data

urlpatterns = [
    path('api/stock', get_stock_data),
]
