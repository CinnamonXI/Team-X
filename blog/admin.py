from django.contrib import admin
from .models import Post, Comment
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'pub_date', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at', 'pub_date', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'pub_date'
    ordering = ('is_published', 'pub_date')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'subject', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'post')
    search_fields = ('name', 'email', 'message', 'subject')
    raw_id_fields = ('post',)
    ordering = ('is_active', 'created_at')
