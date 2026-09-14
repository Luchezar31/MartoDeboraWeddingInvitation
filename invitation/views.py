from django.http import HttpResponse
from django.shortcuts import render

def invitationview(request):
    return render(request,'invitation.html')
