# Generated by Django 4.1.5 on 2023-04-20 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_alter_services_category_alter_services_skills'),
        ('chat', '0003_remove_chat_chat_room_delete_chatroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='job_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.services'),
        ),
    ]
