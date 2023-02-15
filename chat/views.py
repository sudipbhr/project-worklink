from django.shortcuts import render
from chat.models import Chat, Notification


# Create your views here.

def chats(request):
    messages = Chat.objects.all()
    template_name= 'chat/chats.html'
    context={
        'messages' : messages
    }
    return render (request, template_name, context)

def notification(request):
    notification=Notification.objects.all()
    templete_name='chat/notification.html'
    print(notification)
    context={
     'alerts':notification
    }
    return render(request, templete_name, context)