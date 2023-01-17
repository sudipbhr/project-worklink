from django.shortcuts import render
from .models import Services, Category

# Create your views here.

def home(request):
    categories = Category.objects.all()
    services = Services.objects.all()
    context={
        'categories': categories,
        'services': services
    }
    return render(request, 'services/home.html', context)

def services_search(request):
    services = Services.objects.all()
    context={
        'text': "Good evening everyone",
        'services': services
    }
    return render(request, 'services/services-search.html', context)


def services_detail(request):
    return render(request, 'services/service-detail.html', context={})