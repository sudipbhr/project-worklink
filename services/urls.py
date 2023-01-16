from django.urls import path
from . import views
# url patterns

urlpatterns = [
    path('', views.home, name="home-page"),
    path('job-search/', views.services_search, name="job-search")
]
