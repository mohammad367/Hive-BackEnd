from django.db import models
from django.conf import settings
from uuid import uuid4
# Create your models here.


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=16)
    birth_date = models.DateField()
    identity_card_number = models.CharField(max_length=10)
    identity_card_image = models.ImageField(null=True)
    birth_certificate_image = models.ImageField(null=True, blank=True)


class Advertisement(models.Model):
    raiser = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    categories = [
        ('G', 'general'),
        ('A', 'animals'),
        ('M', 'medicine'),
        ('ED', 'education'),
        ('F', 'family'),
        ('ND', 'natural_disaster'),
        ('HC', 'human_catastrophe'),
        ('B', 'businesses'),
        ('EN', 'environment')
    ]
    category = models.CharField(max_length=30, choices=categories, default=1)
    amount = models.FloatField()
    collected_amount = models.FloatField()
