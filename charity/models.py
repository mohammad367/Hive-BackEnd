from django.db import models

# Create your models here.


class Advertisement(models.Model):
    pass
    # profile_photo = models.ImageField()

# advertise model:
# amount
# collected_amount
# title
# description
# raiser -> foreignkey: donatordonatee
# photo


# donatordonatee model:
# user -> content_type - core-models-user
# birth_date
# is_verified default=false
# identity_code *
# account_number *
# postal_code */
# identity_cart_photo */
# identity_cart_photo1 */
