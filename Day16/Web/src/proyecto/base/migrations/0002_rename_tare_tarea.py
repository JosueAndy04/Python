# Generated by Django 5.2 on 2025-04-17 23:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tare',
            new_name='Tarea',
        ),
    ]
