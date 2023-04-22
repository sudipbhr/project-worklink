from django.contrib import admin
from .models import UserVerification

# Register your models here.
class UserVerificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'email_verified', 'phone_verified', 'email_verified_at', 'phone_verified_at')

admin.site.register(UserVerification, UserVerificationAdmin)