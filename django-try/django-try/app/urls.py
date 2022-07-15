


from django import views

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('index',views.index),
    path('about/<int:id>',views.about)
]