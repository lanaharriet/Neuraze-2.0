from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.feed, name='feed'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('react/<int:post_id>/<int:value>/', views.react_post, name='react_post'),
    path('delete-post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('delete-comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
