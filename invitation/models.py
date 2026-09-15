

from django.db import models

class WeddingGuest(models.Model):
    first_name = models.CharField(
        max_length=50,
    )
    last_name= models.CharField(
        max_length=50,
    )
    email = models.EmailField()

    attending = models.BooleanField(
        default=False
    )

    dietary_restrictions = models.TextField(
        blank=True,
        null=True
    )

    