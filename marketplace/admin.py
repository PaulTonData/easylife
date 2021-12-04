from django.contrib import admin

from .models import Posting, Photo

admin.site.register(Posting)
admin.site.register(Photo)