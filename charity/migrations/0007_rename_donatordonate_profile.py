# Generated by Django 4.1.5 on 2023-02-04 05:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('charity', '0006_alter_donatordonate_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DonatorDonate',
            new_name='Profile',
        ),
    ]