from django.contrib import admin
from .views import *

admin.site.site_header= "PWE"

admin.site.index_title =' Blog app for PG'
admin.site.register(Contact)
