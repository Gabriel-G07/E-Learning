# Generated by Django 3.2.13 on 2024-08-29 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='Position',
            field=models.CharField(max_length=50),
        ),
    ]
