
from django.shortcuts import render,redirect
from django.contrib import messages
from account.forms import UserProfileForm,UserEducationForm,UserSkillsForm
from .models import User,UserEducation,UserSkills
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url = '/auth/login/')
def user_profile(request):
    user = get_object_or_404(User, username = request.user.username)
    print(user)
    form = UserProfileForm(instance = user )
    education, created = UserEducation.objects.get_or_create(user = user)
    user_education = UserEducationForm(instance = education)
    skill, created = UserSkills.objects.get_or_create(user = user)
    user_skill = UserSkillsForm(instance = skill)
    if request.method == "POST":
        form = UserProfileForm(request.POST or None, request.FILES ,instance = user)
        user_education = UserEducationForm(request.POST or None, instance = education)
        user_skill = UserSkillsForm(request.POST or None, instance = skill)

        if form.is_valid() and user_education.is_valid() and user_skill.is_valid():
            form.save()
            user_education.save()
            user_skill.save()
            messages.success(request, "profile updated successfully")
            return redirect('user-profile')

    template_name= 'account/user-profile.html'
    context= {
        'form' : form,
        'user_education' : user_education,
        'user_skill' :user_skill,
        'user' : user        
    }
    return render(request, template_name, context)


    