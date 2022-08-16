from ast import Add
from django.urls import path
from . import views
from .views import Home, PostDetail, AddPost, UpdatePostViews, DeleteViews, posts




urlpatterns = [
    path('', Home.as_view(), name = "home"),
    path('about', views.about, name="about"),
    path('post/<int:pk>', PostDetail.as_view(), name="postdetail"),
    path('add_post', AddPost.as_view(), name='add_post'),
    path('post/edite/<int:pk>', UpdatePostViews.as_view(), name = "update_post" ),
    path('post/<int:pk>/remove', DeleteViews.as_view(), name = "delete_post" ),
    path('posts', posts.as_view(), name = "posts"),

]