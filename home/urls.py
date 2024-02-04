from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name="home"),
    path('loginUser',views.loginUser,name="login"),
    path('lougout',views.logoutUser,name="logoutUser"),
    path('createpost',views.createPost,name="createPost"),
]