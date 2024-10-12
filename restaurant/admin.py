from django.contrib import admin
from .models import Booking, Menu

# Register your models here.
admin.site.site_title = "Restaurant Admin"
admin.site.site_header = "Restaurant Admin"
admin.site.index_title = "Welcome to Restaurant Admin"
admin.site.register(Booking)
admin.site.register(Menu)
