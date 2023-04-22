from django.contrib import admin
from .models import Notification, Chat

# Register your models here.
class ChatAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'message', 'status', 'created_at', 'job_id')

admin.site.register(Chat, ChatAdmin)
admin.site.register(Notification)
