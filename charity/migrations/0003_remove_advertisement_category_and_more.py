# Generated by Django 4.1.5 on 2023-02-16 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0002_advertisement_image_donatordonate_avatar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='category',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='collected_amount',
        ),
    ]
