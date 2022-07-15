
from django import views

from django.urls import path
from .views import  register,loginm,logOut


urlpatterns = [
   path("register", register),
   path("login",loginm),
   path('logout',logOut)
]