from django.urls import path
from . import views
app_name ='jobs'

urlpatterns = [
     path('sighnup/',views.sighnup , name='sighnup'),
     path('profile/',views.profile , name='profile'),
     path('profile/edit/',views.profile_edit , name='profile_edit'),
]