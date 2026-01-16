from django.urls import path
from .views import *


urlpatterns = [
    path('', WelcomePage, name='WlP'),
    path('home/', HomePage, name='HP'),
    path('login/', AuthPage, name='LnP'),
    path('register/', RegPage, name='RgP'),
    path('logout/', LogoutView, name='LtP'),
    path('group/events/', EventsPage, name='EvP'),
    path('group/announcements/', AnnPage, name='AnP'),
    path('group/about/', GroupPage, name='GrP'),
]