from account.models import User
from django.shortcuts import get_object_or_404
from chat.models import Notification, Chat


def header_info(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, username = request.user.username)
        notifications= Notification.objects.filter(receiver=user, status='unseen').order_by('-created_at')[:5]
        # unseen messages
        unseen_messages = Chat.objects.filter(receiver=request.user, status='Unseen').count()
        # unseen notifications
        unseen_notifications = Notification.objects.filter(receiver=request.user, status='unseen').count()
        return {
            'notifications':notifications,
            'no_unseen_messages':unseen_messages,
            'no_unseen_notif':unseen_notifications,
            }
    else:
        return {}
    

  