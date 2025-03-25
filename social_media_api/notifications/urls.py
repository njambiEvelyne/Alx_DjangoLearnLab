from django.urls import path
from .views import LikePostView, UnlikePostView, NotificationListView


urlpatterns = [
    path('posts/<int:post_id>/like/', LikePostView.as_view(), name='like_post'),
    path('posts/<int:post_id>/unlike/', UnlikePostView.as_view(), name='unlike_post'),
    path('notifications/', NotificationListView.as_view(), name='notifications'),

]
