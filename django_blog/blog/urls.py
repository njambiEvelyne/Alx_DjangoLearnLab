from django.urls import path
from .views import (
    CommentCreateView, CommentDeleteView, CommentUpdateView, 
    edit_profile_view, register_view, login_view, logout_view, 
    profile_view, home_view, posts_view,
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView,
    post_list, post_detail, posts_by_tag, search_posts
)

urlpatterns = [
    # Home and User Authentication
    path("", home_view, name="home"),
    path("posts/", posts_view, name="posts"),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_view, name="profile"),
    path("profile/edit/", edit_profile_view, name="edit_profile"),

    # Blog Post URLs
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), 
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comment URLs (Using Class-Based Views)
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='add_comment'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),

    # Tagging and Search URLs
    path('tag/<slug:slug>/', posts_by_tag, name='posts_by_tag'),
    path('search/', search_posts, name='search_posts'),
]
