from django.contrib import admin
from .models import Notification, Chat

# Register your models here.
admin.site.register(Chat)
admin.site.register(Notification)
