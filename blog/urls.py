from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import re_path

urlpatterns = [
    path("", views.PostList, name="home"),
    path("post_details/<pk>", views.PostDetail, name="post_details"),
    path("index", views.PostList, name="home"),
    re_path(r'^about/$', views.About, name="about"),
    path("edit_post/<pk>", views.edit_post, name="edit_post"),
    path(
        "delete_confirmation/<pk>",
        views.delete_confirmation,
        name="delete_confirmation"
        ),
    path("add_post/<pk>", views.add_post, name="add_post"),
    # path("comment/<pk>", views.PostDetail, name="submit"),
]
