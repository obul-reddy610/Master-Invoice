# Generated by Django 5.1.6 on 2025-03-21 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='role',
        ),
        migrations.AlterField(
            model_name='profile',
            name='firm_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
