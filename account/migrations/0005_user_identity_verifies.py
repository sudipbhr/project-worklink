# Generated by Django 4.1.5 on 2023-02-21 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_user_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='identity_verifies',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
