from django.db import models

# Create your models here.


# advertise model

# donatordonatee model
from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    raiser = models.ForeignKey()
    amout = models.CharField()
    collected_amount = models.CharField()
   
    amount = models.FloatField()
    collected_amount = models.FloatField()
    raiser = models.ForeignKey(to, on_delete)

class DonatoDonatee(models.Model):
    account_number = models.CharField(max_length=16)
    identity_card_number = models.CharField()
    identity_card_image = models.ImageField()
    identity_card_image2 = models.ImageField()

    birth_date = models.DateField()
    Identity_card_number = models.CharField(max_length=10)
    Identity_card_photo = models.ImageField()
    Identity_card_photo1 = models.ImageField()
    account_number = models.CharField(max_length=16)
# user -> content_type: Core_User
