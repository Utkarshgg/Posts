from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.showthis, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('/freak', views.freak, name='freak'),
    path('yes', views.yes, name='yes'),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
    path('signup', views.handleSignup, name="handleSignup"),
]