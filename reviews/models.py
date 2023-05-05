from django.db import models
from account.models import User
from services.models import Services
from django.db.models import Avg

# Create your models here.
class JobReviews(models.Model):
    # model for job reviews
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer')
    doer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doer')
    service = models.OneToOneField(Services, on_delete=models.CASCADE, related_name='reviewed_service')
    review = models.TextField()
    rating = models.IntegerField(default='0')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.rating)

    class Meta:
        verbose_name_plural = 'Job reviews'

    @property
    def avg_rating(self):
        return self.rating.aggregate(Avg('rating'))['rating__avg']