from django.urls import path
from . import views
# url patterns

urlpatterns = [
    path('', views.chats, name="chat"),
    path('notification/',views.notification, name='notification')

]