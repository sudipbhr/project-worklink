from django.shortcuts import render, get_object_or_404
from .models import Services, Category
from django.contrib import messages
# Create your views here.

def home(request):
    categories = Category.objects.all() 
    services = Services.objects.all()
    context={
        'categories': categories,
        'services': services,
    }
    return render(request, 'services/home.html', context)

def services_search(request):
    services = Services.objects.all()
    context={
        'services': services
    }
    return render(request, 'services/services-search.html', context)


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
  
  
def services_detail(request, id):
    services = get_object_or_404(Services, id=id)

    template_name='services/service-detail.html'
    context={
        'services': services
    }
    return render(request, template_name, context)

def user_dashboard(request):
    template_name='services/dashboard.html'
    context={}

