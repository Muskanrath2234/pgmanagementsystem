from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [

    path('', home, name='home'),
    path('about/', about, name='about' ),
    path('contact/', contact, name='contact'),
    path('user_login/', user_login, name='user_login'),
    path('leave-request/', leave_request, name='leave_request'),
    path('admin_leave-requests/', admin_leave_requests, name='admin_leave_requests'),
    path('my-leave-requests/', my_leave_requests, name='my_leave_requests'),
    path('leave-request/<int:leave_id>/delete/', delete_leave_request, name='delete_leave_request'),
    path('leave-request/<int:leave_id>/update/', update_leave_request, name='update_leave_request'),


]
