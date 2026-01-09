from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage, name='HP'),
    path('group/events/', EventsPage, name='EvP'),
    path('group/announcements/', AnnPage, name='AnP'),
    path('group/about/', GroupPage, name='GrP'),
]