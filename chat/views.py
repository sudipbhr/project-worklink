from django.shortcuts import render
from .models import Notification
from django.contrib.auth.decorators import login_required
from chat.models import Chat
from django.db.models import Q

# Create your views here.

def chats(request, sender_id=None, receiver_id=None, chat_id=None):
    chats = Chat.objects.filter(Q(sender=request.user) | Q(receiver=request.user))
    template_name= 'chat/chats.html'
    print(chats)
    context={
        'chats':chats
    }
    return render (request, template_name, context)


@login_required(login_url = '/auth/login/')
def notification(request):
    templete_name='chat/notification.html'
    context={}
    return render(request, templete_name, context)