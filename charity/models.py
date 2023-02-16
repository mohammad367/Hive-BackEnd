from django.db import models
from django.conf import settings
from uuid import uuid4
# Create your models here.


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=16)
    avatar = models.ImageField(upload_to = 'profile/avatar/' , null = True , blank = True)
    birth_date = models.DateField()
    identity_card_number = models.CharField(max_length=10)
    identity_card_image = models.ImageField(upload_to = 'profile/identity_card_image/')
    birth_certificate_image = models.ImageField(upload_to = 'profile/birth_certificate_image/')


class Advertisement(models.Model):
    raiser = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to = 'ads/', null = True , blank = True)
    amount = models.FloatField()

