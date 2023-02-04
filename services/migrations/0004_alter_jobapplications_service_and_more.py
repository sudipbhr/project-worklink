# Generated by Django 4.1.5 on 2023-02-04 07:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0003_remove_jobapplications_service_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplications',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='services.services'),
        ),
        migrations.AlterField(
            model_name='jobapplications',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to=settings.AUTH_USER_MODEL),
        ),
    ]
