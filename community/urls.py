from django.urls import path
from . import views

app_name = "community"

urlpatterns = [
    path("", views.community_home, name="home"),
    path("post/<int:post_id>/", views.view_post, name="view_post"),
    path("post/<int:post_id>/comment/", views.add_comment, name="add_comment"),
    path("post/<int:post_id>/like/", views.toggle_like, name="toggle_like"),
    path("create/", views.create_post, name="create_post"),
]
