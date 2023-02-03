from django.db import models
# should not import from other apps, use content type instead
from django.conf import settings
# Create your models here.


class DonatorDonate(models.Model):
    donator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=16)
    birth_date = models.DateField()
    identity_card_number = models.CharField(max_length=10)
    identity_card_image = models.ImageField(null=True)
    birth_certificate_image = models.ImageField(null=True)


class Advertisement(models.Model):
    raiser = models.ForeignKey(DonatorDonate, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    categories = [
        (1, 'general'),
        (2, 'animals'),
        (3, 'medicine'),
        (4, 'education'),
        (5, 'family'),
        (6, 'natural_disaster'),
        (7, 'human_catastrophe'),
        (8, 'businesses'),
        (9, 'environment')
    ]
    category = models.CharField(max_length=30, choices=categories, default=1)
    amount = models.FloatField()
    collected_amount = models.FloatField()
