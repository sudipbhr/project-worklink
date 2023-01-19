from django.shortcuts import render
from .models import Services, Category
from django.contrib import messages
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
        'services': services
    }
    return render(request, 'services/services-search.html', context)


def services_detail(request):
    template_name='services/service-detail.html'
    context={}
    return render(request, template_name, context)

def user_dashboard(request):
    template_name='services/dashboard.html'
    context={}
    return render(request, template_name, context)

def about_us(request):
    template_name = 'about-us.html'
    context={}
    return render(request, template_name, context)

def contact_us(request):
    template_name= 'contact-us.html'
    context={}
    return render (request, template_name, context)

def categories(request):
    template_name= 'services/categories.html'
    context={}
    return render (request, template_name, context)