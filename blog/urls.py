from django.urls import path
from . import views
from django.conf.urls import url, include
from django.urls import re_path

urlpatterns = [
    path("", views.PostList, name="home"),
    path("post_details/<pk>", views.PostDetail, name="post_details"),
    path("index", views.PostList, name="home"),
    re_path(r'^about/$', views.About, name="about"),
    path("edit_post/<slug:slug>", views.edit_post, name="edit_post"),
    path('delete_post/<slug:slug>', views.delete_post, name="delete_post"),
    path("add_post", views.add_post, name="add_post"),
    path("choose_category", views.choose_category, name="choose_category"),
]
