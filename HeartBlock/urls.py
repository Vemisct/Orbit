from django.urls import path, include
from .views import *

urlpatterns = [
    # Google Auth (Allauth)
    path('accounts/', include('allauth.urls')),
    path('', WelcomePage, name='WlP'),
    path('home/', HomePage, name='HP'),
    path('login/', AuthPage, name='LnP'),
    path('register/', RegPage, name='RgP'),
    path('logout/', LogoutView, name='LtP'),
    path('group/about/', GroupPage, name='GrP'),
    path('profile/', ProfilePage, name='PrP'),
    path('group/<int:group_id>/', GroupPage, name='GrInP'),
    path('group/join/<int:group_id>/', JoinGroup, name='JnGrP'),
    path('group/about/<int:group_id>/', AboutGroupPage, name='AbGrP'),
    path('group/leave/', LeaveGroup, name='LvGrP'),
    path('group/mygroup', MemberGroupPage, name='GrMP'),
    path('settings/', SettingsPage, name='StP'),
    path('comment/delete/<int:pk>/', DeleteComment, name='DlCm'),
    path('profile/edit/', ProfileEditPage, name='PrEdP'),
    path('shop/', ShopPage, name='ShP'),
    path('payment-success/', PaymentSuccess, name='PaySuccess'),
    path('member/<int:member_id>/', AboutMember, name='AbMP'),
]