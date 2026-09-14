from django.urls import path

from invitation import views

urlpatterns = [
    path('',views.invitationview,name='invitation')
]