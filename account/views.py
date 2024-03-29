
from django.shortcuts import render, redirect
from django.contrib import messages
from account.forms import UserProfileForm, UserEducationForm, UserSkillsForm
from .models import User, UserEducation, UserSkills
from chat.models import Notification
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from services.models import Services

# Create your views here.


@login_required(login_url='/auth/login/')
def user_profile_edit(request):
    user = get_object_or_404(User, username=request.user.username)
    form = UserProfileForm(instance=user)
    skill, created = UserSkills.objects.get_or_create(user=user)
    user_skill = UserSkillsForm(instance=skill)

    if request.method == "POST":
        level = request.POST.get('level') or None
        degree = request.POST.get('degree') or None
        college = request.POST.get('college_university_name') or None
        end_date = request.POST.get('end_date') or None
        edu_description = request.POST.get('edu_description') or None
        if level and degree and college:
            education = UserEducation.objects.create(
                user=user,
                level=level,
                degree=degree,
                college_university_name=college,
                end_date=end_date,
                edu_description=edu_description
            )
            education.save()
            messages.success(request, "Education added successfully")
            return redirect('profile')
        form = UserProfileForm(request.POST or None,
                               request.FILES, instance=user)
        # user_education = UserEducationForm(request.POST or None, instance = education)
        user_skill = UserSkillsForm(request.POST or None, instance=skill)
        document = request.FILES.get('document')
        if document:
            user.identity_proof = document
            user.save()
            messages.success(request, "Document uploaded successfully")
            redirect('dashboard')

        if form.is_valid() and user_skill.is_valid():
            form.save()
            # user_education.save()
            user_skill.save()
            messages.success(request, "Profile updated successfully")
            return redirect('profile')

    template_name = 'account/edit-user-profile.html'
    context = {
        'form': form,
        'user_skill': user_skill,
        'user': user,
        'forms': [form, user_skill]
    }
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def user_profile(request):
    user = get_object_or_404(User, id=request.user.id)
    education = UserEducation.objects.filter(
        user_id=user).order_by('-end_date')
    jobs = Services.objects.filter(job_holder_id=user, status='completed')
    template_name = 'account/profile.html'
    skills = UserSkills.objects.get_or_create(user=user)

    context = {
        'user': user,
        'skills': skills,
        'education': education,
        'jobs': jobs
    }
    return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def manage_users(request):
    if request.user.role == 'Admin':
        users = User.objects.all().exclude(username=request.user.username or role ==
                                           'Admin' or is_superuser == True).order_by('-date_joined')
        if request.method == "POST":
            user_id = request.POST.get('user')
            status = request.POST.get('status')
            user = User.objects.get(id=user_id)
            user.user_status = status
            user.save()
            messages.success(request, "User status updated successfully")
            return redirect('manage-users')
        template_name = 'account/manage-users.html'
        context = {
            'users': users
        }
        return render(request, template_name, context)


@login_required(login_url='/auth/login/')
def disqualify_document(request, id):
    user = get_object_or_404(User, id=id)
    user.identity_verifies = False
    user.save()
    messages.success(request, "Identity document disqualified")
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/auth/login/')
def verify_document(request, id):
    user = get_object_or_404(User, id=id)
    user.identity_verifies = True
    user.save()
    messages.success(request, "Identity document verified")
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/auth/login/')
def del_education(request, id):
    education = get_object_or_404(UserEducation, id=id)
    education.delete()
    messages.success(request, "Education deleted successfully")
    return redirect(request.META.get('HTTP_REFERER'))
