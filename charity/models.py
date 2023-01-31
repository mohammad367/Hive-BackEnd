from django.db import models

# Create your models here.


# advertise model

# donatordonatee model
from django.db import models


class Advertisement(models.Model):
    pass
# amount
# collected amount
# raiser -> foreignkey: DonatorDonatee
# title
# description


class DonatoDonatee(models.Model):
    pass
# birth_date
# Identity_card_number
# Identity_card_photo
# Identity_card_photo1
# account_number
# user -> content_type: Core_User
