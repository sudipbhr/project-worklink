from django.db import models
from account.models import User

# Create your models here.
class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.TextField()
    attachment = models.FileField(upload_to='chat/', blank=True, null=True)
    STATUS = (
        ('Unseen', 'Unseen'),
        ('Seen', 'Seen')
    )
    status = models.CharField(max_length=100, choices=STATUS, default='Unseen')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name_plural = 'Chats'

class Notification(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='noti_sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='noti_receiver')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name_plural = 'Notifications'