from django.contrib import admin
from .models import Payment, BuyPoints, LoadBalance
# Register your models here.

admin.site.register(Payment)
admin.site.register(BuyPoints)
admin.site.register(LoadBalance)