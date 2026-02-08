from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('feed/', views.feed, name='feed'),

    # FIX: allow -1
    path('post/<int:post_id>/react/<str:value>/', views.react_post, name='react_post'),
    
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
]
