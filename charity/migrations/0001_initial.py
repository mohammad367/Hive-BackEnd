# Generated by Django 4.1.5 on 2023-02-02 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DonatorDonate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('account_number', models.CharField(max_length=16)),
                ('birth_date', models.DateField()),
                ('identity_card_number', models.CharField(max_length=10)),
                ('identity_card_image', models.ImageField(upload_to='')),
                ('birth_certificate_image', models.ImageField(upload_to='')),
                ('donator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.CharField(choices=[(1, 'general'), (2, 'animals'), (3, 'medicine'), (4, 'education'), (5, 'family'), (6, 'natural_disaster'), (7, 'human_catastrophe'), (8, 'businesses'), (9, 'environment')], default=1, max_length=30)),
                ('amount', models.FloatField()),
                ('collected_amount', models.FloatField()),
                ('raiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charity.donatordonate')),
            ],
        ),
    ]