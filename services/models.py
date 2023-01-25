from django.db import models
from account.models import User


# Create your models here.
class JobSkills(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Job skills'

# model for job category
class Category(models.Model):
    name = models.CharField(max_length=100)
    skills=models.ManyToManyField(JobSkills, blank=True)
    image= models.ImageField(upload_to='category/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

    def no_of_jobs(self):
        return self.services_set.all().count()


class Services(models.Model):
    # model for jobs in online job portal
    title = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.IntegerField(default='0', help_text="Enter amount in rupees")
    duration= models.IntegerField(default='1', help_text="Enter time in days")
    STATUS=(
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('hiring', 'Hiring')
    )
    status = models.CharField(max_length=100, choices=STATUS, default='hiring')
    category = models.ManyToManyField(Category, blank=True)
    skills =models.ManyToManyField(JobSkills, blank=True)
    vacancy = models.IntegerField(help_text="Enter number of vacancies", default='1')
    posted_by= models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='services')
    location =models.CharField(max_length=200)
    image = models.ImageField(upload_to='services/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Services'





