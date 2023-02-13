from django.shortcuts import render

# Create your views here.
def chats(request):
    template_name= 'chat/chats.html'
    context={}
    return render(request, template_name, context)

def notification(request):
    templete_name='chat/notification.html'
    context={}
    return render(request, templete_name, context)