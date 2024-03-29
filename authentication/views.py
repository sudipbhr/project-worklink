from django.shortcuts import render, redirect, HttpResponse
from account.models import User, Points, UserBalance
from authentication.models import UserVerification, UserOTP
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib import messages
from django.core.mail import send_mail
import random
from datetime import datetime, timedelta
from django.utils import timezone
from django.conf import settings as setting
from django.contrib.auth.decorators import login_required
from services.views import send_sms

# Create your views here.
def send_otp(user):
    # generate 6 digit random number
    try:
        otp=random.randint(10000,99999)
        user_otp = UserOTP.objects.create(user=user, otp=otp)
        user_otp.save()
        subject = "OTP verfication"
        message = """
Dear Sir/Madam,
Do NOT SHARE your OTP/Password with anyone..
Your OTP is {otp}

If you have any queries, Please contact us at,

Project WorkLink,
Bagar,Pokhara, Nepal.
Phone # 977-01-4523333
Email Id: support@worklink.com.np

Warm Regards,
Project WorkLink
"Connecting Job Seekers and Providers"
                        """
        message=message.format(otp=otp)
        from_email = setting.EMAIL_HOST_USER
        recepient_list = [user.email]
        mail= send_mail(subject, message, from_email, recepient_list, fail_silently=False)
        sms= send_sms(user.phone_number, message)
        if mail:
            print("mail sent")
        else:
            print("mail not sent")
        if sms:
            print("sms sent")
        else:
            print("sms not sent")
            
    except Exception as e:
        print(e)
        return False
        

def user_login(request):
    if request.method == "POST":
        user_email = request.POST["email"]
        user_password = request.POST["password"]
        user_exists = User.objects.filter(Q(email=user_email) | Q(phone_number=user_email)).first()
        if user_exists:
            user = authenticate(request, username=user_exists.username, password=user_password)
            if user:
                user_points = Points.objects.filter(user=user).exists()
                user_balance = UserBalance.objects.filter(user=user).exists()
                if not user_points:
                    user_points = Points.objects.create(user=user)
                    user_points.save()
                if not user_balance:
                    user_balance = UserBalance.objects.create(user=user)
                    user_balance.save()
                
                is_verified = UserVerification.objects.filter(user=user_exists).first()
                if is_verified.email_verified == False | is_verified.phone_verified == False:
                    if send_otp(user):
                        print(send_otp)
                        print("hello")
                    else:
                        print("not working")
                    messages.warning(request, "User must be verified first")
                    context = {
                        'user': user
                    }
                    return render(request,'authentication/verify.html', context)
                else:
                    login(request, user)
                    messages.success(request, "Logged in successfully")
                    return redirect('dashboard')
            else:
                messages.error(request, "Invalid credentials")
                return redirect('login')
        else:
            messages.error(request, "Couldnot find user, please register first")
            return redirect('login')
    
    if request.user.is_authenticated:
        return redirect('home-page')

    template_name = "authentication/login.html"
    context = {}
    return render(request, template_name, context)

def user_register(request):
    user_type=[]
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        user_email = request.POST["email"]
        user_phone= request.POST["phone"]
        user_type = request.POST['user_type']
        user_password = request.POST["password1"]
        user_password2 = request.POST["password2"]
        user_exists = User.objects.filter(Q(email=user_email), Q(first_name=first_name), Q(last_name=last_name) 
                            | Q(phone_number=user_phone), Q(first_name=first_name), Q(last_name=last_name)).exists()
        if user_exists:
            messages.error(request, "User already exists")
            return redirect('register')
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
            user = User.objects.create_user(first_name=first_name, last_name=last_name,  username=username, email=user_email, password=user_password, phone_number=user_phone, role=user_type)
            user.save()
            user_verification = UserVerification.objects.create(user=user)
            user_verification.save()
            messages.success(request, "User created successfully")
            return redirect('login')

    template_name = "authentication/register.html"
    context = {}
    return render(request, template_name, context)

def user_verification(request):
    if request.method == "POST":
        otp = request.POST.get("otp")
        print(otp)
        user = request.POST.get("user")
        user_otp = UserOTP.objects.filter(user_id=user).last()
        print(user_otp.otp)
        if otp == str(user_otp.otp):
            user_verification = UserVerification.objects.filter(user_id=user).last()
            user_verification.email_verified = True
            user_verification.save()
            messages.success(request, "User verified successfully")
            return redirect('login')
        else:
            messages.error(request, "Invalid OTP")
            return redirect('verification')
    template_name = "authentication/verify.html"
    return render(request, template_name)


@ login_required(login_url='/auth/login/')
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home-page')


@ login_required(login_url='/auth/login/')
def change_password(request):
    if request.method == "POST":
        old_password = request.POST["old_password"]
        new_password = request.POST["new_password"]
        new_password2 = request.POST["new_password2"]
        user = User.objects.filter(id=request.user.id).first()

        if user.check_password(old_password):
            if new_password == new_password2:
                user.set_password(new_password)
                user.save()
                messages.success(request, "Password changed successfully")
                return redirect('dashboard')
            else:
                messages.error(request, "Passwords don't match")
                return redirect('change-password')
        else:
            messages.error(request, "Invalid password")
            return redirect('change-password')
        

    template_name='authentication/change-password.html'
    context={}
    return render(request, template_name, context)

# def forgot_password(request):
#     if request.method == "POST":
#         user_email_phone = request.POST["email_or_phone"]
#         user_exists = User.objects.filter(Q(email=user_email_phone) | Q(phone_number=user_email_phone)).first()
#         if user_exists:
#             if send_otp(user_exists):
#                 print("hello")
#             else:
#                 print("not working")
#             messages.success(request, "OTP sent successfully")
#             return render(request, 'authentication/verify.html', {'user': user_exists})
#         else:
#             messages.error(request, "No user found with the given details")
#             return redirect('forgot-password')

#     template_name='authentication/forgot-password.html'
#     context={}
#     return render(request, template_name, context)

