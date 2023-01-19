# Generated by Django 4.1.5 on 2023-01-16 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='category/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='JobSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Job skills',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('amount', models.IntegerField(default='0', help_text='Enter amount in rupees')),
                ('duration', models.IntegerField(default='1', help_text='Enter time in days')),
                ('status', models.CharField(choices=[('active', 'Active'), ('completed', 'Completed'), ('hiring', 'Hiring')], default='hiring', max_length=100)),
                ('vacancy', models.IntegerField(default='1', help_text='Enter number of vacancies')),
                ('location', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='services/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(blank=True, to='services.category')),
                ('posted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('skills', models.ManyToManyField(blank=True, to='services.jobskills')),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='skills',
            field=models.ManyToManyField(blank=True, to='services.jobskills'),
        ),
    ]
