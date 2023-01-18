from django.urls import path
from . import views
# url patterns

urlpatterns = [
    path('', views.home, name="home-page"),
    path('services/', views.services_search, name="service-search"),
    path('services/<str:id>/service-detail/', views.services_detail, name="service-detail"),
    path('dashboard/', views.user_dashboard, name="dashboard"),
]

