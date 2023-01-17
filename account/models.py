from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager
from .degree_list import DEGREE_LIST


# Create your models here.
class User(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True)
    ROLES_CHOICES = (
        ('servicee', 'Service Provider'),
        ('servicer', 'Service Seeker'),
        ('admin', 'Admin')
    )
    role = models.CharField(max_length=20, choices = ROLES_CHOICES, default='servicee')
    USER_STATUS_CHOICES= (
        ('active', 'Active'),
        ('suspended', 'Suspended')
    )
    user_status = models.CharField(max_length=20, choices = USER_STATUS_CHOICES, default='active')
    GENDER_CHOICES= (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Do not specify')
    )
    gender = models.CharField(max_length=20, choices= GENDER_CHOICES, blank=True)
    avatar = models.ImageField(upload_to='avatar/', default='avatar/default.webp', blank=True)
    experience = models.IntegerField(default=0, help_text="Duration in years", blank=True)
    address = models.CharField(max_length=100, blank=True)
    REQUIRED_FIELDS=[]

    objects = UserManager()

    def __str__(self):
        return self.email

class Points(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='points')
    points = models.IntegerField(default='0')
    remarks = models.CharField(max_length=200, blank=True)
    updated_on= models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.phone_number + ' has ' + str(self.points) + ' points'

    class Meta:
        verbose_name_plural = "Points"
class UserEducation(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='education')
    LEVEL_CHOICES = (
        ('illiterate', 'Illiterate'),
        ('primary', 'Primary Level'),
        ('seconday', 'Secondary Level'),
        ('higher_secondary', 'Higher Secondary Level'),
        ('vocational', 'Vocational'),
        ('bachelor', 'Bachelor Degree'),
        ('master','Master Degree'),
        ('doctorate','Doctorate'),
    )
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES, default='primary')
    degree= models.CharField(max_length=50, choices=DEGREE_LIST, blank=True )
    add_degree= models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.get_full_name() + ' has ' + self.level + ' education'

    class Meta:
        verbose_name_plural = "User Education"
class UserSkills(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='skill')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'User skills'


