from django.contrib import admin
from django.urls import path,include
from blog import views



urlpatterns = [
    path('', views.index, name="index"),
    path('', views.single, name="single"),
    path('login', views.loginuser ,name="login"),
    path('logout', views.logoutuser ,name="logout"),
    path('signup', views.signup ,name="signup"),
    path('addarticle', views.addarticle ,name="addarticle"),
]
