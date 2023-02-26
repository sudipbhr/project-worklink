# Generated by Django 4.1.5 on 2023-02-21 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_userskills_user_userskills_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userskills',
            name='user',
        ),
        migrations.AddField(
            model_name='userskills',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skill', to=settings.AUTH_USER_MODEL),
        ),
    ]
