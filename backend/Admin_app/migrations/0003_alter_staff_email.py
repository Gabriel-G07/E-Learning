# Generated by Django 3.2.13 on 2024-08-29 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0002_alter_staff_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='Email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
