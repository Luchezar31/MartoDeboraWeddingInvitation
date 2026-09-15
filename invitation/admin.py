from django.contrib import admin

from invitation.models import WeddingGuest


@admin.register(WeddingGuest)
class WeddingGuestAndmin(admin.ModelAdmin):
    pass

