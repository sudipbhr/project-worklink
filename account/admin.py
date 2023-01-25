from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm


class MyUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'role', 'avatar')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')})
    )
    # this is for update view
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
        ),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'role', 'avatar')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),

    )
    # this is for create view
    ordering = ('first_name',)
    list_display = ['first_name', 'last_name', 'role', 'phone_number', 'email']



# Register your models here.
admin.site.register(User, MyUserAdmin)
admin.site.register(Points)
admin.site.register(UserEducation)
admin.site.register(UserSkills)
admin.site.register(UserBalance)
