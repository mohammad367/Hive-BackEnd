from django.db import models
from core.models import User
# Create your models here.


class Advertisement(models.Model):
    raiser = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    amount = models.FloatField()
    collected_amount = models.FloatField()
    collected_amount = models.FloatField()


class DonatorDonate(models.Model):
    donator = models.ForeignKey(User, on_delete=models.PROTECT)
    account_number = models.CharField(max_length=16)
    birth_date = models.DateField()
    identity_card_number = models.CharField(max_length=10)
    identity_card_image = models.ImageField()
    birth_certificate_image = models.ImageField()
