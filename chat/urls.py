from django.urls import path
from . import views
# url patterns

urlpatterns = [
    path('', views.chats, name='chat'),
    path('notification/',views.notification, name='notification'),
    path('notification/<str:noti_id>/', views.notification_detail, name='notification-detail'),
    path('<str:chat_id>/<str:id>/', views.single_chat, name="user-chat"),

]