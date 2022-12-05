from django.urls import path
from . import views
from django.conf.urls import url 

urlpatterns = [
    path("", views.PostList, name="home"),
    path("post_details", views.PostDetail, name="post_details"),
    # path("index", views.PostList, name="home"),
    # path("about", views.PostList, name="about"),
    url(r'^about/$', views.About, name="about"),
    # url(r'^$',),
]
