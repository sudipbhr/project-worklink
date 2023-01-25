from django.urls import path
from . import views
# url patterns

urlpatterns = [
    path('', views.user_profile, name="user-profile"),
]