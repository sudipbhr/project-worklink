from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/auth/login/')
def buy_points(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        amount = float(amount)
        if amount > request.user.user_balance.balance:
            messages.error(request, 'You do not have enough balance to buy points')
            return redirect('buy-points')
        else:
            request.user.user_balance.balance -= amount
            request.user.user_balance.save()
            points=amount
            request.user.points.points += points
            request.user.points.save()
            messages.success(request, 'You have successfully bought points')
            return redirect(request.META.get('HTTP_REFERER'))            
       
    template_name = 'payment/buy-points.html'
    context={}
    return render(request, template_name, context)

def notification(request):
    template_name='payment/notification.html'
    context={}
    return render(request, template_name, context)