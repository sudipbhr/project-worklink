from django.shortcuts import render
from .models import Notification
from django.contrib.auth.decorators import login_required
from chat.models import Chat

# Create your views here.

def chats(request):
    messages = Chat.objects.all()
    template_name= 'chat/chats.html'
    context={
        'messages' : messages
    }
    return render (request, template_name, context)


@login_required(login_url = '/auth/login/')
def notification(request):
    templete_name='chat/notification.html'
    context={}
    return render(request, templete_name, context)