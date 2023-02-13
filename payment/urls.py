from django.urls import path
from . import views

urlpatterns = [
    path('buy-points/', views.buy_points, name='buy-points'),
   
]