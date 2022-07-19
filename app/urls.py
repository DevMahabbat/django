


from django import views

from django.urls import path

from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('about/<int:id>',views.about),
    path('dashboard',views.dashboard,name="dashboard"),
    path('addarticle',views.addArticle),
    path('article/<int:id>',views.detail,name="detail"),
    path('update/<int:id>',views.updateArticle,name="update"),
]
