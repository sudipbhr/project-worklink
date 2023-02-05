# Generated by Django 4.1.5 on 2023-02-04 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_jobapplications_service_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplications',
            name='status',
            field=models.CharField(choices=[('Hiring', 'Hiring'), ('Hired', 'Hired'), ('Rejected', 'Rejected')], default='Hiring', max_length=100),
        ),
    ]
