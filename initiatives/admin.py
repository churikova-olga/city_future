from django.contrib import admin

from .models import Initiative, Comment

admin.site.register(Initiative)
admin.site.register(Comment)