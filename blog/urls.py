from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'BlogHome'),
    path('handlecomment/',views.handlecomment, name = 'HandleComment'),
    path('<str:slug>',views.blogPost, name = 'blogPost'),
    
]