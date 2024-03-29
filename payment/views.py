from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from payment.models import Payment, BuyPoints, LoadBalance
from datetime import datetime
from django.http import JsonResponse
import json
import random


# Create your views here.
@login_required(login_url='/auth/login/')
def buy_points(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        amount = float(amount)
        if amount > request.user.user_balance.balance:
            messages.error(request, 'You do not have enough balance to buy points')
            return redirect('load-balance')
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

@login_required(login_url='/auth/login/')
def load_balance(request):
    template_name = 'payment/load-balance.html'
    if request.method == 'POST':
        amount = request.POST.get('amount')
        remarks = request.POST.get('remarks')
        amount = float(amount)
        transcation_id = datetime.now().strftime("%Y%m%d%H%M%S")+str(request.user.id)
        load = LoadBalance.objects.create(user=request.user, amount=amount, remarks=remarks, identity=transcation_id, status='pending')
        load.save()
        context={
            'amount': amount,
            'transcation_id': transcation_id,
            'remarks': remarks,
            'product_url': 'http://worklink.com.np',
            'condition': 'true',
        }
        return render(request, template_name, context)
    return render(request, template_name)

@login_required(login_url='/auth/login/')
def payment_success(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        payment = LoadBalance.objects.get(identity=body['transcation_id'], user=body['user'], amount=body['amount'])
        payment.status = 'completed'
        payment.save()
        request.user.user_balance.balance += payment.amount
        request.user.user_balance.save()
        messages.success(request, 'You have successfully loaded your balance')
        return redirect('buy-points')
