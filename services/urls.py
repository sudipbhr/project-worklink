from django.urls import path
from . import views
# url patterns

urlpatterns = [
    path('', views.home, name="home-page"),
    path('services/', views.services_search, name="service-search"),
    path('services/<str:id>/service-detail/', views.services_detail, name="service-detail"),
    path('service-search-map/',views.service_search_map, name="service-search-map"),
    path('candidates/candidate-detail/', views.candidate_detail, name="candidate-detail"),
    path('error-page/', views.error_page, name="404-page"),
    path('dashboard/', views.user_dashboard, name="dashboard"),

