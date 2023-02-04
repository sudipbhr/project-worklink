from django.shortcuts import render, get_object_or_404, redirect
from .models import Services, Category, JobApplications
from django.contrib import messages
from .forms import PostJobForm, CategoryForm, JobSkillForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    categories = Category.objects.all()[:6]
    services = Services.objects.all().order_by('-amount')[:8]
    context={
        'categories': categories,
        'services': services,
    }
    template_name='services/home.html'
    return render(request, template_name, context)

@login_required(login_url='/auth/login/')
def services_search(request):
    if request.user.role == 'Service Seeker':
        return redirect('dashboard')
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
    has_applied = JobApplications.objects.filter(user=request.user, service=services).exists()
    no_of_applications = JobApplications.objects.filter(service=services).count()
    template_name='services/service-detail.html'
    if request.method == 'POST':
        points = request.POST.get('points')
        resume = request.FILES.get('resume')
        if int(points) != 10:
            messages.error(request, 'Invalid points')
            return redirect('service-detail', id=services.id)
        else:
            job_apply = JobApplications.objects.create(
                user=request.user,
                service= services,
                resume=resume,
                        )
            job_apply.save()
            request.user.points.points -= int(points)
            request.user.points.save()
            messages.success(request, 'Job application sent successfully')
            return redirect('manage-job')
    context={
        'services': services,
        'has_applied': has_applied,
        'no_of_applications': no_of_applications,
    }
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def user_dashboard(request):
    # jobs posted by user
    jobs_posted = JobApplications.objects.filter(user=request.user).count()
    applied_jobs = JobApplications.objects.filter(user=request.user).count()
    template_name='services/dashboard.html'
    context={
        'jobs_posted': jobs_posted,
        # 'applied_jobs': applied_jobs,
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
                    print('form is valid')
                    add_post_by=form.save(commit=False)
                    add_post_by.posted_by = request.user
                    if add_post_by.save():
                        print('job posted successfully')
                        form.save_m2m()
                        request.user.points.points -= 10
                        request.user.points.save()
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
    applied_jobs = JobApplications.objects.filter(user=request.user)
    posted_jobs = Services.objects.filter(posted_by=request.user)
    for job in posted_jobs:
        no_of_applications = JobApplications.objects.filter(service=job).count()
        
    template_name='services/manage-job.html'
    context={
        'applied_jobs': applied_jobs,
        'posted_jobs': posted_jobs,
        'no_of_applications': no_of_applications,
    }
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


@ login_required(login_url='/auth/login/')
def add_category(request):

    category_add= CategoryForm()
    if request.method== "POST": 
        category_add = CategoryForm(request.POST or None, request.FILES)
        if category_add.is_valid():
            category_add.save()
            messages.success(request, "category added successfully")
            return redirect ('dashboard')

    template_name='services/add-category.html'
    context={
        'form': category_add,
    }
    return render(request, template_name, context)



@ login_required(login_url='/auth/login/')
def job_skill(request):

    form = JobSkillForm()
    if request.method == "POST":
        form = JobSkillForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "jobskill added successfully")
            return redirect ('dashboard')
    template_name = 'services/job-skill.html'
    context = {
        'form' : form,
    
    }
    return render(request, template_name, context)

