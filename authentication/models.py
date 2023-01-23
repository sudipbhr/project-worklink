from django.db import models
from account.models import User

# Create your models here.
class UserVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    email_verified_at = models.DateTimeField(blank=True, null=True)
    phone_verified_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class UserOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.IntegerField()
    otp_created_at = models.DateTimeField(auto_now_add=True)
    otp_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username



