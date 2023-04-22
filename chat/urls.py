from django.urls import path
from . import views
# url patterns

urlpatterns = [
    path('', views.chats, name='chat'),
    path('<str:chat_id>/<str:id>/', views.single_chat, name="user-chat"),
    path('notification/',views.notification, name='notification'),

]