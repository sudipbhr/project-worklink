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


def service_search_map(request):
    template_name='services/service-search-map.html'
    context={}
    return render(request, template_name, context)


def candidate_detail(request):
    template_name='services/candidate-detail.html'
    context={}
    return render(request, template_name, context)

def error_page(request):
  return render(request, 'services/error-page.html', context={})