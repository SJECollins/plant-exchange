from django.contrib import admin
from .models import BlogPost, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(BlogPost)
class PostAdmin(SummernoteModelAdmin):
    list_filter = ('status', 'created_on')
    list_display = ('title','status', 'created_on')
    search_fields = ('title', 'content')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'post', 'created_on',)
    list_filter = ('created_on',)
    search_fields = ('author', 'content')
