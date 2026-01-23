from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.TopicListView.as_view(), name='topic_list'),
    path('<int:pk>/', views.TopicDetailView.as_view(), name='topic_detail'),
    path('create/', views.TopicCreateView.as_view(), name='topic_create'),
    path('<int:pk>/post/', views.PostCreateView.as_view(), name='post_create'),
    path('<int:topic_pk>/post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('<int:topic_pk>/post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('topic/<int:pk>/delete/', views.TopicDeleteView.as_view(), name='topic_delete'),
]