from django.shortcuts import render, get_object_or_404, redirect
from .models import Services, Category, JobApplications, JobSkills
from account.models import User
from chat.models import Chat, Notification
from django.contrib import messages
from .forms import PostJobForm, CategoryForm, JobSkillForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import ServicesFilter
from django.db.models import Q

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


def salary_range():
    salaries = Services.objects.values_list('amount', flat=True).distinct()
    low_salary = min(salaries)
    high_salary = max(salaries)
    ranges = []
    # create a range of salaries
    while low_salary <= high_salary:
        range_filter = "Rs."+ str(round(low_salary, -3)) + " - Rs." + str(round((low_salary + 4000), -3))
        ranges.append(range_filter)
        low_salary += 4000
    return ranges

@login_required(login_url='/auth/login/')
def services_search(request):
    if request.user.role == 'Service Seeker':
        return redirect('dashboard')
    categories = Category.objects.all()
    services = Services.objects.all()
    services_count = services.count()
    services_filter = ServicesFilter(request.GET, queryset=services)
    paginator = Paginator(services, 9)
    page = request.GET.get('page')
    services = paginator.get_page(page)
    
    context={
        'services': services,
        'total_services': services_count,
        'categories': categories,
        'services_filter': services_filter,
        'locations': Services.objects.values_list('location', flat=True).distinct(),
        'ranges': salary_range(),
    }
    return render(request, 'services/services-search.html', context)


@login_required(login_url='/auth/login/')
def search(request):
    template_name = 'services/services-search.html'
    # all categories
    categories = Category.objects.all()
    if request.method == 'GET':
        q = request.GET.get('query')
        category = request.GET.get('category')
        area = request.GET.get('area')
        salary = request.GET.get('salary')
        if salary:
            salary = salary.split(' - ')
            min_salary = int(salary[0].replace('Rs.', ''))
            max_salary = int(salary[1].replace('Rs.', ''))
            salary_services = Services.objects.filter(
                Q(amount__gte = min_salary) & Q(amount__lte = max_salary)
            )
        else:
            salary_services = []
            
        if q:
            search_services = Services.objects.filter(
                Q(title__icontains=q)| Q(location__icontains=q)|Q(category__name__icontains = q) |
                Q(skills__name__icontains = q) | Q(description__icontains = q)
            )
        else:
            search_services=[]

        if category:
            category_services = Services.objects.filter(
                Q(category__name__icontains = category)
            )
        else:
            category_services = []

        if area:
            area_services = Services.objects.filter(
                Q(location__icontains = area)
            )
        else:
            area_services = []
        
        services = set(search_services).union(set(category_services).union(set(area_services)).union(set(salary_services)))
        context={
            'services': services,
            'categories': categories,
            'filter_name': q or category or area or salary,
            'total_services': len(services),
            'locations': Services.objects.values_list('location', flat=True).distinct(),
            'ranges': salary_range(),

        }
        return render(request, template_name, context)
    


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


def privacy_policy(request):
    template_name= 'privacy-policy.html'
    context={}
    return render (request, template_name, context)


def faq(request):
    template_name= 'faq.html'
    context={}
    return render (request, template_name, context)

def categories(request):
    categories = Category.objects.all()
    template_name= 'services/categories.html'
    context={
        'categories': categories,
    
    }
    return render (request, template_name, context)


@login_required(login_url='/auth/login/')
def post_job(request):
    title = "Post a new job"
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
    elif request.user.points.points < 10:
        messages.error(request, 'You do not have enough points to post job')
        return redirect('buy-points')
    else:
        messages.error(request, 'You cannot post job')
        return redirect('dashboard')
    context={
            'title': title,
            'form':form,
            'forms': [form]
            }
    template_name='services/post-job.html'
    return render(request, template_name, context)

@login_required(login_url='/auth/login/')
def update_job(request, job_id):
    job_id = get_object_or_404(Services, id=job_id)
    form = PostJobForm(instance=job_id)
    if request.method == 'POST':
        form = PostJobForm(request.POST, request.FILES, instance=job_id)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job updated successfully')
            return redirect('manage-job')
    context={
        'form': form,
        'forms': [form]
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
            job_in_service.job_holder = User.objects.get(id=user)
            job_in_service.save()
            job.status = jobstatus
            job.save()
            notification = Notification.objects.create(
                receiver=job.user, sender= job.service.posted_by,
                message='Dear {job_holder}, you have been hired for {job}. We look forward for your successful job. Thank you for choosing WorkLink'.format(job_holder=job.service.job_holder.first_name+ " "+ job.service.job_holder.last_name,job=job.service.title),
            )
            notification.save()
            chat = Chat.objects.create(
                sender=job.service.posted_by, receiver=job.user,
                message='Dear {job_holder}, you have been hired for {job}. We look forward for your successful job. Thank you for choosing WorkLink'.format(job_holder=job.service.job_holder.first_name+ " "+ job.service.job_holder.last_name, job=job.service.title),
                job_id=job.service
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
        'forms': [category_add]
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
        'forms': [form]
    
    }
    return render(request, template_name, context)

def review(request):
    template_name='reviews/review.html'
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

# quering the jobs of the particular skill
@login_required(login_url='/auth/login/')
def skill_jobs(request, id):
    jobs = Services.objects.filter(skills=id)
    skill_name = JobSkills.objects.get(id=id)
    template_name='services/services-search.html'
    context={
        'services': jobs,
        'filter_name': skill_name.name,
    }
    return render(request, template_name, context)

# quering the jobs of the particular category
@login_required(login_url='/auth/login/')
def category_jobs(request, id):
    jobs = Services.objects.filter(category=id)
    category_name = Category.objects.get(id=id)
    template_name='services/services-search.html'
    context={
        'services': jobs,
        'filter_name': category_name.name,
    }
    return render(request, template_name, context)