from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name="login"),
    path('register/', views.user_register, name="register"),
    path('verify/', views.user_verification, name="verification"),
    path('logout/', views.user_logout, name="logout"),
    path('otp/', views.send_otp, name='otp'),
    path('change-password/', views.change_password, name="change-password"),

]
