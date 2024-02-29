from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [

    path('', home, name='home'),
    path('about/', about, name='about' ),
    path('contact/', contact, name='contact'),
    path('user_login/', user_login, name='user_login'),



]

