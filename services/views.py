from django.shortcuts import render, get_object_or_404, redirect
from .models import Services, Category
from django.contrib import messages
from .forms import PostJobForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    categories = Category.objects.all() 
    services = Services.objects.all()
    context={
        'categories': categories,
        'services': services,
    }
    template_name='services/home.html'
    return render(request, template_name, context)

@login_required(login_url='/auth/login/')
def services_search(request):
    categories = Category.objects.all()
    services = Services.objects.all()
    context={
        'services': services,
        'categories': categories,
    }
    return render(request, 'services/services-search.html', context)

@login_required(login_url='/auth/login/')
def service_search_map(request):
    template_name='services/service-search-map.html'
    context={}
    return render(request, template_name, context)

@login_required(login_url='/auth/login/')
def candidate_detail(request):
    template_name='services/candidate-detail.html'
    context={}
    return render(request, template_name, context)

def error_page(request):
  return render(request, 'services/error-page.html', context={})
  

@login_required(login_url='/auth/login/') 
def services_detail(request, id):
    services = get_object_or_404(Services, id=id)

    template_name='services/service-detail.html'
    context={
        'services': services
    }
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def user_dashboard(request):

    # jobs posted by user
    jobs_posted = Services.objects.filter(posted_by=request.user.id).count()



    template_name='services/dashboard.html'
    context={
        'jobs_posted': jobs_posted,
    }
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
    categories = Category.objects.all()
    template_name= 'services/categories.html'
    context={
        'categories': categories
    }
    return render (request, template_name, context)


@login_required(login_url='/auth/login/')
def post_job(request):
    try:
        form = PostJobForm() or None
        if request.user.can_post_job == True:
            if request.method == 'POST':
                form = PostJobForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Job posted successfully')
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Error posting job')
                    return redirect('post-job')
        elif request.user.points.points < 10:
            messages.error(request, 'You dont have enough points to post job')
            return redirect('buy-points')
        else:
            messages.error(request, 'You cannot post job')
            return redirect('dashboard')
    except Exception as e:
        print(e)
    context={
                'form':form
            }
    template_name='services/post-job.html'
    return render(request, template_name, context)

@ login_required(login_url='/auth/login/')
def manage_job(request):
    template_name='services/manage-job.html'
    context={}
    return render(request, template_name, context)


@ login_required(login_url='/auth/login/')
def sidebar(request):
    template_name='services/sidebar.html'
    context={}
    return render(request, template_name, context)

   
def manage_seeker(request):
    template_name='services/manage-seeker.html'
    context={}
    return render(request, template_name, context)


@ login_required(login_url='/auth/login/')
def my_profile(request):
    template_name='services/my-profile.html'
    context={}
    return render(request, template_name, context)

@ login_required(login_url='/auth/login/')
def change_password(request):
    template_name='services/change-password.html'
    context={}
    return render(request, template_name, context)







        
    
    
