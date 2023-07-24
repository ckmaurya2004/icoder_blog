from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'Home'),
    path('contact/',views.contact, name = 'Contact'),
    path('about/',views.about, name = 'About'),
    path('search/',views.search, name = 'Search'),
    path('login/',views.handlerlogin, name = 'handlerlogin'),
    path('logout/',views.handlerlogout, name = 'handlerlogout'),
    path('signup/',views.handlesignup, name = 'handlesignup')# type: ignore


]
