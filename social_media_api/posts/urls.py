from django.urls import path
from .views import PostListView, PostCreateView, PostRetrieveUpdateDestroyView, like_post, unlike_post

urlpatterns = [
    path('feed/', PostListView.as_view(), name='post-feed'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),
    path('posts/<int:pk>/like/', like_post, name='post-like'),
    path('posts/<int:pk>/unlike/', unlike_post, name='post-unlike'),
]
