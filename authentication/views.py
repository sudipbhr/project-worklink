from django.shortcuts import render, redirect
from account.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib import messages


# Create your views here.

def login(request):
    if request.method == "POST":
        user_email = request.POST["email"]
        user_password = request.POST["password"]

        user_exists = User.objects.filter(Q(email=user_email) | Q(phone_number=user_email)).first()
        if user_exists:
            user=authenticate(request, email=user_exists.email, password=user_password)
            login(request, user)
            messages.success(request, "Logged in successfully")
            print("Logged in successfully")
            return redirect('home-page')
        else:
            messages.error(request, "User does not exist")
            print("User does not exist")
            return redirect('home-page')

        template_name = "authentication/login.html"
        context = {}
        return render(request, template_name, context)

