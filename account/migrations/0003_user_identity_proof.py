# Generated by Django 4.1.5 on 2023-02-08 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_profession'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='identity_proof',
            field=models.ImageField(blank=True, upload_to='identity_proof/'),
        ),
    ]
