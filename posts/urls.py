from django.urls import path
from .views import tag_list, create_tag

urlpatterns = [
    path('tags/', tag_list, name='tag_list'),
    path('tags/create/', create_tag, name='create_tag'),
]