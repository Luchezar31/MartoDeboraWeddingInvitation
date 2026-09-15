

from django import forms

from invitation.models import WeddingGuest


from django import forms
from .models import WeddingGuest

class WeddingGuestForm(forms.ModelForm):
    class Meta:
        model = WeddingGuest
        fields = ('first_name', 'attending', 'dietary_restrictions')
        labels = {
            'first_name': 'Вашето име',
            'attending': 'Ще присъствате ли?',
            'dietary_restrictions': 'Хранителни предпочитания',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Име и фамилия'
            }),
            'attending': forms.Select(choices=[
                ('', 'Моля, изберете...'),
                (True, 'С удоволствие ще присъствам'),
                (False, 'За съжаление няма да мога'),
            ]),
            'dietary_restrictions': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'Алергии, вегетарианство и др. (незадължително)'
            }),
        }

            