from django.db import models
# should not import from other apps, use content type instead
from core.models import User
# Create your models here.


class DonatorDonate(models.Model):
    # -> use content type instead of import user from Core App
    donator = models.ForeignKey(User, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=16)
    avatar = models.ImageField(upload_to = 'profile/avatar/')
    birth_date = models.DateField()
    identity_card_number = models.CharField(max_length=10)
    identity_card_image = models.ImageField(upload_to = 'profile/identity_card_image/')
    birth_certificate_image = models.ImageField(upload_to = 'profile/birth_certificate_image/')


class Advertisement(models.Model):
    raiser = models.ForeignKey(DonatorDonate, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to = 'ads/')
    categories = [
        ('G','general'),
        ('A','animals'),
        ('M','medicine'),
        ('ED','education'),
        ('F','family'),
        ('ND','natural_disaster'),
        ('HC','human_catastrophe'),
        ('B','businesses'),
        ('EN','environment')
    ]
    category = models.CharField(max_length=30,choices=categories, default=1)
    amount = models.FloatField()
    collected_amount = models.FloatField()
