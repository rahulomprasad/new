from django.contrib import admin
from django.urls import path,include
from blog import views



urlpatterns = [
    path('', views.index, name="index"),
    path('single', views.single, name="single"),
    path('login', views.loginuser ,name="login"),
    path('logout', views.logoutuser ,name="logout"),
    path('signup', views.signupuser ,name="signup"),
    path('addarticle', views.addarticlenew ,name="addarticle"),
]
