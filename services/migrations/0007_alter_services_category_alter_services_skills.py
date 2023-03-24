# Generated by Django 4.1.5 on 2023-03-21 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_alter_jobapplications_applied_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='category', to='services.category'),
        ),
        migrations.AlterField(
            model_name='services',
            name='skills',
            field=models.ManyToManyField(blank=True, related_name='skills', to='services.jobskills'),
        ),
    ]
