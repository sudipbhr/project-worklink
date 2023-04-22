from django.urls import path
from . import views

urlpatterns = [
    path('buy-points/', views.buy_points, name='buy-points'),
    path('load-balance/', views.load_balance, name='load-balance'),
    path('payment-success/', views.payment_success, name='payment-success'),
]