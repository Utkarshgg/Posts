from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    
    path('', views.blogHome, name='blogHome'),
    # path('<str:slug>', views.blogPost, name='blogPost'),
    path('<int:user_id>/', views.blogHome1, name='blogHome1'),
    path('t/<int:sno>/', views.delete_Post, name = 'delete_Post'),
    path('new1/',views.postme, name='postme' )
    # path('login', views.handeLogin, name="handleLogin"),
    # path('logout', views.handelLogout, name="handleLogout"),
]