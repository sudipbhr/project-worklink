from django.shortcuts import render

# Create your views here.
def chats(request):
    template_name= 'chat/chats.html'
    context={}
    return render(request, template_name, context)