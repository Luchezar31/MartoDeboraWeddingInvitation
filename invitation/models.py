

from django.db import models

from invitation.choices import AttendingTextChoices

class WeddingGuest(models.Model):
    first_name = models.CharField(
        max_length=50,
    )
    last_name= models.CharField(
        max_length=50,
    )
    email = models.EmailField()

    attending = models.BooleanField(
        blank=False,
        null=True,
        choices=AttendingTextChoices.choices,
        default=AttendingTextChoices.PENDING,
    )

    dietary_restrictions = models.TextField(
        blank=True,
        null=True
    )
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'