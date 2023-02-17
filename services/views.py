from django.shortcuts import render, get_object_or_404, redirect
from .models import Services, Category, JobApplications
from account.models import User
from chat.models import Chat, Notification
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
def candidate_detail(request, id):
    user = get_object_or_404(User, id=id)
    template_name='services/candidate-detail.html'
    context={
        'user': user,
    }
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
            if request.user.can_apply_job == True:
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
            else:
                messages.error(request, 'You cannot apply for job')
                return redirect('service-detail', id=services.id)
    context={
        'services': services,
        'has_applied': has_applied,
        'no_of_applications': no_of_applications,
    }
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def user_dashboard(request):
    # jobs posted by user
    jobs_posted = Services.objects.filter(posted_by=request.user).count()
    applied_jobs = JobApplications.objects.filter(user=request.user).count()
    total_applications = JobApplications.objects.filter(service__posted_by=request.user).count()
    template_name='services/dashboard.html'
    context={
        'jobs_posted': jobs_posted,
        'applied_jobs': applied_jobs,
        'total_applications': total_applications,
    }
    return render(request, template_name, context)


# this function load the about us page
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
def post_job(request, job_id=None):
    if job_id is not None:
        job_id = get_object_or_404(Services, id=job_id)
        form = PostJobForm(instance=job_id)
        if request.method == 'POST':
            form = PostJobForm(request.POST, request.FILES, instance=job_id)
            if form.is_valid():
                form.save()
                messages.success(request, 'Job updated successfully')
                return redirect('dashboard')
            else:
                messages.error(request, 'Error updating job')
                return redirect('post-job')
    else:
        form = PostJobForm() or None
        if request.user.can_post_job == True:
            if request.method == 'POST':
                form = PostJobForm(request.POST, request.FILES)
                if form.is_valid():
                    add_post_by=form.save(commit=False)
                    add_post_by.posted_by = request.user
                    add_post_by.save()
                    form.save_m2m()
                    request.user.points.points -= 10
                    request.user.points.save()
                    messages.success(request, 'Job posted successfully')
                    return redirect('manage-job')
                else:
                    messages.error(request, 'Error posting job')
                    return redirect('post-job')
        elif request.user.points.points < 10:
            messages.error(request, 'You dont have enough points to post job')
            return redirect('buy-points')
        else:
            messages.error(request, 'You cannot post job')
            return redirect('dashboard')
    context={
                'form':form
            }
    template_name='services/post-job.html'
    return render(request, template_name, context)

@ login_required(login_url='/auth/login/')
def manage_job(request):
    applied_jobs = JobApplications.objects.filter(user=request.user)
    posted_jobs = Services.objects.filter(posted_by=request.user)        
    template_name='services/manage-job.html'
    context={
        'applied_jobs': applied_jobs,
        'posted_jobs': posted_jobs,
    }
    return render(request, template_name, context)


@ login_required(login_url='/auth/login/')
def sidebar(request):
    template_name='services/sidebar.html'
    context={}
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def manage_applicant(request, id):
    if request.method == 'POST':
        jobstatus = request.POST.get('status')
        user = request.POST.get('applicant')
        service = request.POST.get('service')
        if jobstatus == 'Hiring':
            job = JobApplications.objects.get(service=service, user=user)
            job.status = jobstatus
            job.save()
            messages.info(request, 'Applicant assigned for hiring')
            return redirect('manage-applicant' , id=job.service.id)
        elif jobstatus == 'Hired':
            job = JobApplications.objects.get(service=service, user=user)
            job_in_service = Services.objects.get(id=service, posted_by=request.user)
            job_in_service.status = 'Active'
            job_in_service.save()
            job.status = jobstatus
            job.save()
            notification = Notification.objects.create(
                receiver=job.user, sender= job.service.posted_by,
                message='You have been hired for {job}'.format(job=job.service.title),
            )
            notification.save()
            chat = Chat.objects.create(
                sender=job.service.posted_by, receiver=job.user,
                message='You have been hired for {job}'.format(job=job.service.title),
            )
            chat.save()
            messages.success(request, 'Applicant hired')
            return redirect('manage-applicant' , id=job.service.id)
        elif jobstatus == 'Rejected':
            job = JobApplications.objects.get(service=service, user=user)
            job.status = jobstatus
            job.save()
            messages.success(request, 'Applicant rejected')
            return redirect('manage-applicant' , id=job.service.id)
        else:
            messages.error(request, 'Error approving applicant')
            return redirect('manage-job')
    applicants = JobApplications.objects.filter(service=id)
    template_name='services/manage-applicant.html'
    context={
        'applicants': applicants,
    }
    return render(request, template_name, context)

def transactions(request):
    template_name = 'services/transactions.html'
    context ={}
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
            messages.success(request, "Jobskill added successfully")
            return redirect ('dashboard')
    template_name = 'services/job-skill.html'
    context = {
        'form' : form,
    
    }
    return render(request, template_name, context)

def review(request):
    template_name='services/review.html'
    context={}
    return render(request, template_name, context)

@login_required(login_url='/auth/login/')
def delete_job(request, id):
    job_applications = JobApplications.objects.filter(service=id, status='Hired')
    if job_applications:
        messages.error(request, 'You cannot delete this job because it has been hired')
        return redirect('manage-job')
    else:
        job = Services.objects.get(id=id)
        job.delete()
        messages.success(request, 'Job deleted successfully')
    return redirect('manage-job')