from django.urls import path
from . import views
# url patterns

urlpatterns = [
    path('', views.home, name="home-page"),
    path('service-search/', views.services_search, name="job-search"),
    path('service-detail/', views.services_detail, name="job-detail"),
    path('service-search-map/',views.service_search_map, name="service-search-map"),
    path('candidates/candidate-detail/', views.candidate_detail, name="candidate-detail"),
    path('error-page/', views.error_page, name="404-page"),
   
]

