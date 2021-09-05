"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = "account"
urlpatterns = [
    path('', views.index),
    path('index', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('review', views.review, name='review'),
    path('pick', views.pick, name='pick'),
    path('change/<int:user_id>', views.change_nickname, name='change'),
]
