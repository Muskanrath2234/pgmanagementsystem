from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [


    path('adminlogin/', adminlogin, name='adminlogin'),
    path('admindash/', admindash, name='admin_dash'),
    path('userregister/', register_user, name='userregister'),
    path('view_all_user/', view_all_users, name='view_all_users'),
    path('profilehome', profilehome, name='profilehome'),
    path('editprofile/', editprofile, name='editprofile'),
    path('user_logout/', user_logout, name='user_logout'),

    path('post/', PostListView.as_view(), name='post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('create_post/', create_post, name='create_post'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),

    path('author/<str:username>/', author_profile, name='author-profile'),

    path('posts/<int:year>/<int:month>/<int:day>/', posts_by_date, name='posts-by-date'),

   ]


