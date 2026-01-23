from django.urls import path
from .views import *


urlpatterns = [
    path('group/events/', EventsPage, name='EvP'),
]