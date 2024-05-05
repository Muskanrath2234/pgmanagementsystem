from django.urls import path
from .views import *

urlpatterns = [
    path('upload_aadhar/', upload_aadhar, name='upload_aadhar'),
    path('result/', result, name='result'),
    path('upload_pan_card/', upload_pan_card, name='upload_pan_card'),
    path('success_page/', success_page, name='success_page'),
    path('Document_view/', Document_view, name='Document_view'),
]