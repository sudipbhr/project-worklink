from django.shortcuts import render
from .models import Notification
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = '/auth/login/')
def chats(request):
    template_name= 'chat/chats.html'
    context={}
    return render(request, template_name, context)

@login_required(login_url = '/auth/login/')
def notification(request):
    notifications = Notification.objects.all()
    template_name= 'chat/notification.html'
    context={
        'n' : notifications
    }
    return render(request, template_name, context)