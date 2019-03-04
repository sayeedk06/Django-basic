from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.home,name = 'home'),
    path('home/', views.home,name = 'home'),
    path('allpost/',views.allpost,name = 'allpost'),
    path('allpost/<pk>/',views.allpost,name = 'allpost_pk'),
    path('allpost/<category>',views.categoryPost,name = 'categoryPost'),
]
