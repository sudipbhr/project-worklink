from django.urls import path
from . import views
# url patterns

urlpatterns = [
    path('', views.chats, name='chat'),
    path('<str:sender_id>/<str:receiver_id>/<str:chat_id>/', views.chats, name="user-chat"),
    path('notification/',views.notification, name='notification'),

]