from django.db import models
from account.models import User

# Create your models here.
class UserVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_verified = models.BooleanField(default=True)
    phone_verified = models.BooleanField(default=True)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    phone_verified_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username



