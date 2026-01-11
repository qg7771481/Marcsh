from django.urls import path
from .views import *

urlpatterns = [
    path('posts/<int:post_id>/comments/', CommentListView.as_view(), name='comment_list'),
    path('posts/<int:post_id>/comments/create/', CommentCreateView.as_view(), name='comment_create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]