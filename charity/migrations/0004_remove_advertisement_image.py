# Generated by Django 4.1.5 on 2023-02-14 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0003_advertisement_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='image',
        ),
    ]
