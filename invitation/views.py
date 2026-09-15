from django.http import HttpResponse
from django.shortcuts import render

from invitation.forms import WeddingGuestForm

def invitationview(request):
    form = WeddingGuestForm(request.POST or None)

    context = {
        'form': form
    }

    return render(request,'invitation.html',context=context)
