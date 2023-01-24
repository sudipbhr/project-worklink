
from django.shortcuts import render

# Create your views here.
def user(request):
    template_name= 'account/user-profile.html'
    context= {}
    return render(request, template_name, context)