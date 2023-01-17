from django.urls import path
from . import views
# url patterns

urlpatterns = [
    path('', views.home, name="home-page"),
    path('service-search/', views.services_search, name="job-search"),
    path('service-detail/', views.services_detail, name="job-detail")
]

