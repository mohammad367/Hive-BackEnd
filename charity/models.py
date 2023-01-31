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
    pass
# amount
# collected amount
# raiser -> foreignkey: DonatorDonatee
# title
# description


class DonatoDonatee(models.Model):
    account_number = models.CharField(max_length=16)
    identity_card_number = models.CharField()
    identity_card_image = models.ImageField()
    identity_card_image2 = models.ImageField()
    pass
# birth_date
# Identity_card_number
# Identity_card_photo
# Identity_card_photo1
# account_number
# user -> content_type: Core_User
