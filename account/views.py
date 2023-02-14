
from django.shortcuts import render,redirect
from django.contrib import messages
from account.forms import UserProfileForm,UserEducationForm,UserSkillsForm
from .models import User,UserEducation,UserSkills
from chat.models import Notification
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = '/auth/login/')
def user_profile_edit(request):
    user = get_object_or_404(User, username = request.user.username)
    form = UserProfileForm(instance = user )
    education, created = UserEducation.objects.get_or_create(user = user)
    user_education = UserEducationForm(instance = education)
    skill, created = UserSkills.objects.get_or_create(user = user)
    user_skill = UserSkillsForm(instance = skill)
    if request.method == "POST":
        form = UserProfileForm(request.POST or None, request.FILES ,instance = user)
        user_education = UserEducationForm(request.POST or None, instance = education)
        user_skill = UserSkillsForm(request.POST or None, instance = skill)
        document = request.FILES.get('document')
        print(document)
        if document:
            user.identity_proof = document
            user.save()
            messages.success(request, "Document uploaded successfully")
            redirect('dashboard')

        if form.is_valid() and user_education.is_valid() and user_skill.is_valid():
            form.save()
            user_education.save()
            user_skill.save()
            messages.success(request, "Profile updated successfully")
            return redirect('user-profile')

    template_name= 'account/edit-user-profile.html'
    context= {
        'form' : form,
        'user_education' : user_education,
        'user_skill' :user_skill,
        'user' : user        
    }
    return render(request, template_name, context)

@login_required(login_url = '/auth/login/')
def user_profile(request):
    user = get_object_or_404(User, username = request.user.username)
    template_name = 'account/profile.html'
    context = {
        'user' : user
    }
    return render(request, template_name, context)

@login_required(login_url = '/auth/login/')
def manage_users(request):
    if request.user.role == 'Admin':
        users = User.objects.all()
        template_name = 'account/manage-users.html'
        context = {
            'users' : users
        }
        return render(request, template_name, context)


@login_required(login_url = '/auth/login/')
def header_info(request):
    user = get_object_or_404(User, username = request.user.username)
    template_name = 'base.html'
    notifications= Notification.objects.filter(receiver=user).order_by('-created_at')
    context = {
        'notifications' : notifications,
    }
    return render(request, template_name, context)