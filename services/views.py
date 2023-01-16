from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'services/home.html', context={})

def services_search(request):
    return render(request, 'services/services-search.html', context={})
