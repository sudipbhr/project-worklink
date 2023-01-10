from django.contrib import admin
from .models import Services, Category, Skills

# Register your models here.
admin.site.register(Category)
admin.site.register(Skills)
admin.site.register(Services)