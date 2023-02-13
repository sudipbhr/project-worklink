from django.shortcuts import render
from chat.models import Chat

# Create your views here.

def chats(request):
    messages = Chat.objects.all()
    template_name= 'chat/chats.html'
    context={
        'messages' : messages
    }
    return render (request, template_name, context)

def notification(request):
    templete_name='chat/notification.html'
    context={}
    return render(request, templete_name, context)