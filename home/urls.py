from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name="home"),
    path('loginUser',views.loginUser,name="login"),
    path('lougout',views.logoutUser,name="logoutUser"),
    path('createpost',views.createPost,name="createPost"),
    path('deletepost', views.deletePost, name="deletePost"),
    path('change', views.change, name="change")
]