from django.shortcuts import render, redirect
from account.models import User
from authentication.models import UserVerification
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib import messages


# Create your views here.

def user_login(request):
    if request.method == "POST":
        user_email = request.POST["email"]
        user_password = request.POST["password"]

        user_exists = User.objects.filter(Q(email=user_email) | Q(phone_number=user_email)).first()
        if user_exists:
            is_verified = UserVerification.objects.filter(user=user_exists).first()
            if is_verified.email_verified == False | is_verified.phone_verified == False:
                messages.error(request, "User is not verified")
                return redirect('login')
            else:
                user = authenticate(request, username=user_exists.username, password=user_password)
                if user:
                    login(request, user)
                    messages.success(request, "Logged in successfully")
                    return redirect('home-page')
                else:
                    messages.error(request, "Invalid credentials")
                    return redirect('login')
        else:
            messages.error(request, "User does not exist with this email or phone number")
            return redirect('login')
    
    if request.user.is_authenticated:
        return redirect('home-page')

    template_name = "authentication/join-as.html"
    context = {}
    return render(request, template_name, context)

def user_register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        user_email = request.POST["email"]
        user_phone= request.POST["phone"]
        user_password = request.POST["password1"]
        user_password2 = request.POST["password2"]
        user_exists = User.objects.filter(Q(email=user_email), Q(first_name=first_name), Q(last_name=last_name) 
                            | Q(phone_number=user_phone), Q(first_name=first_name), Q(last_name=last_name)).exists()
        if user_exists:
            messages.error(request, "User already exists")
            return redirect('login')
        elif (user_password != user_password2):
            messages.error(request, "Passwords don't match")
            return redirect('register')
        elif user_email=="" and user_phone=="":
            messages.error(request, "Email or phone number is required")
            return redirect('register')
        else:
            if user_email:
                username = user_email.lower()
            else:
                username = user_phone
            user = User.objects.create_user(first_name=first_name, last_name=last_name,  username=username, email=user_email, password=user_password, phone_number=user_phone)
            user.save()
            user_verification = UserVerification.objects.create(user=user)
            user_verification.save()
            messages.success(request, "User created successfully")
            return redirect('login')
    if request.user.is_authenticated:
        return redirect('home-page')

    template_name = "authentication/register.html"
    context = {}
    return render(request, template_name, context)


def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home-page')