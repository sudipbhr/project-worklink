from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError


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

    @property
    # no of jobs in a category
    def no_of_jobs(self):
        return self.category.all().count()

    def skills_of_category(self):
        return self.skills.all()
    
   

class Services(models.Model):
    from account.models import User
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
    category = models.ManyToManyField(Category, blank=True, related_name='category')
    skills =models.ManyToManyField(JobSkills, blank=True, related_name='skills')
    vacancy = models.IntegerField(help_text="Enter number of vacancies", default='1')
    posted_by= models.ForeignKey(User, on_delete=models.CASCADE, related_name='services', null=True)
    job_holder = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_holder', null=True, blank=True)
    location =models.CharField(max_length=200)
    image = models.ImageField(upload_to='services/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Services'

    @property
    def no_of_applications(self):
        return self.services.all().count()
    
    @property
    def employee_chat_url(self):
        return reverse('user-chat', args=[self.id, self.posted_by.id])
    
    @property
    def employer_chat_url(self):
        return reverse('user-chat', args=[self.id, self.job_holder.id])
    

            
    
class JobApplications(models.Model):
    
    from account.models import User
    # model for job applications
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applicants')
    service = models.ForeignKey(Services, on_delete= models.CASCADE, related_name='services', null=True)
    STATUS=(
        ('Hiring', 'Hiring'),
        ('Hired', 'Hired'),
        ('Rejected', 'Rejected')
    )
    status = models.CharField(max_length=100, choices=STATUS, default='Hiring')
    applied_on = models.DateTimeField(auto_now_add=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + ' applied for ' + self.service.title

    class Meta:
        verbose_name_plural = 'Job applications'


class Inquries(models.Model):
    name = models.CharField(max_length=100, help_text="Enter your name")
    email = models.EmailField(help_text="Enter your email")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name_plural = 'Inquries'
