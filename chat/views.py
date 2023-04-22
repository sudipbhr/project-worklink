from django.shortcuts import render
from .models import Notification
from django.contrib.auth.decorators import login_required
from chat.models import Chat
from account.models import User
from django.db.models import Q
from services.models import Services
from django.shortcuts import get_object_or_404

# Create your views here.

def chats(request, sender_id=None, receiver_id=None, chat_id=None):
    jobs = Services.objects.filter(Q(posted_by=request.user) | Q(job_holder=request.user))   
    chats= [] 
    for job in jobs:
        message = Chat.objects.filter(Q(sender=request.user) | Q(receiver=request.user), job_id=job.id).order_by('-created_at').first()
        if message:
            chats.append(message)
    template_name= 'chat/chats.html'
    messages = Chat.objects.filter(Q(sender=sender_id, receiver=receiver_id) | Q(sender=receiver_id, receiver=sender_id))
    messages = messages.order_by('-created_at')
    context={
        'chats':chats,
    }
    return render (request, template_name, context)


@login_required
def single_chat(request, chat_id, id):
    jobs = Services.objects.filter(Q(posted_by=request.user) | Q(job_holder=request.user))   
    chats= [] 
    for job in jobs:
        message = Chat.objects.filter(Q(sender=request.user) | Q(receiver=request.user), job_id=job.id).order_by('-created_at').first()
        if message:
            chats.append(message)
    
    # get all the messages
    msgs = Chat.objects.filter(Q(job_id=chat_id), Q(sender=request.user) | Q(receiver=request.user)).order_by('-created_at')
    for msg in msgs:
        if msg.status == 'Unseen':
            msg.status = 'Seen'
            msg.save()
    if request.method == 'POST':
        # find the receiver id
        receiver_id = id
        message = request.POST.get('message')
        chat = Chat.objects.create(
            sender=request.user,
            receiver=User.objects.get(id=receiver_id),
            message = message,
            job_id = Services.objects.get(id=chat_id)
        )
        chat.save()
        
    template_name= 'chat/single-chat.html'
    context={
        'chats':chats,
        'msgs':msgs,
        'chat_id':chat_id,
    }
    return render(request, template_name, context)

@login_required(login_url = '/auth/login/')
def notification(request):
    templete_name='chat/notification.html'
    notifications= Notification.objects.filter(receiver=request.user).order_by('-created_at')
    context={
        'alerts':notifications,
    }
    return render(request, templete_name, context)


@login_required(login_url = '/auth/login/')
def notification_detail(request, id):
    templete_name='chat/notification_detail.html'
    notification= get_object_or_404(id=id)
    context={
        'notification':notification,
    }
    return render(request, templete_name, context)