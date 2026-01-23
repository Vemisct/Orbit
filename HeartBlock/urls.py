from django.urls import path
from .views import *


urlpatterns = [
    path('', WelcomePage, name='WlP'),
    path('home/', HomePage, name='HP'),
    path('login/', AuthPage, name='LnP'),
    path('register/', RegPage, name='RgP'),
    path('logout/', LogoutView, name='LtP'),
    path('group/announcements/', AnnPage, name='AnP'),
    path('group/about/', GroupPage, name='GrP'),
    path('profile/', ProfilePage, name='PrP'),
    path('group/<int:group_id>/', GroupPage, name='GrInP'),
    path('group/join/<int:group_id>/', JoinGroup, name='JnGrP'),
    path('group/leave/', LeaveGroup, name='LvGrP'),
    path('group/mygroup', MemberGroupPage, name='GrMP'),
    path('settings/', SettingsPage, name='StP'),
]