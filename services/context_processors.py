from account.models import User
from django.shortcuts import get_object_or_404
from chat.models import Notification


def header_info(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, username = request.user.username)
        notifications= Notification.objects.filter(receiver=user).order_by('-created_at')[:5]
        return {
            'notifications':notifications
            }
    else:
        return {}
  