# Generated by Django 4.1.5 on 2023-01-21 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userverification',
            name='email_verified',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='userverification',
            name='phone_verified',
            field=models.BooleanField(default=True),
        ),
    ]