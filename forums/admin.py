from django.contrib import admin
from .models import Forum, Discussion, Post


admin.site.register(Forum)
admin.site.register(Discussion)
admin.site.register(Post)

