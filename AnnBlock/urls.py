from django.urls import path
from .views import *

urlpatterns = [
    path('group/announcements/', AnnPage, name='AnP'),
    path('group/announcements/create/', CreateAnn, name='AnnCr'), 
    path('group/announcements/<int:pk>/', AnnDetailPage, name='AnnDet'), 
    path('group/announcements/delete/<str:obj_type>/<int:pk>/', DeleteObject, name='DelObj'),
]