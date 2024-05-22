from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    AboutView,
    add_comment
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),                           # URL pattern for displaying list of posts
    path('about/', AboutView.as_view(), name='about'),                            # URL pattern for the about view
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),         # URL pattern for displaying individual post details
    path('post/new/', PostCreateView.as_view(), name='post_create'),              # URL pattern for creating a new post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),  # URL pattern for updating an existing post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # URL pattern for deleting a post
    path('post/<int:post_id>/comment/', add_comment, name='add_comment'),
    # add more URL patterns here as needed
]
