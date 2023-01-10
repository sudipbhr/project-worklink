from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Skills(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Skills'

# model for job category
class Category(models.Model):
    name = models.CharField(max_length=100)
    skills=models.ManyToManyField(Skills, blank=True, null=True)
    image= models.ImageField(upload_to='category/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Services(models.Model):
    # model for jobs in online job portal
    title = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.IntegerField()
    duration= models.DurationField(blank=True, null=True, default='1 day')
    STATUS=(
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('hiring', 'Hiring')
    )
    status = models.CharField(max_length=100, choices=STATUS, default='hiring')
    category = models.ManyToManyField(Category, blank=True, null=True)
    skills =models.ManyToManyField(Skills, null=True, blank=True)
    vacancy = models.IntegerField()
    posted_by= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    location =models.CharField(max_length=200)
    image = models.ImageField(upload_to='services/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Services'





