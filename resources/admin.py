from django.contrib import admin
from .models import Article, Video, Document

# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'is_published', 'created_at', 'updated_at')
    list_filter = ('is_published', 'created_at', 'category', 'tags', 'author', 'updated_at')
    search_fields = ('title', 'author', 'category', 'description', 'tags')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'video', 'is_published', 'created_at', 'updated_at')
    list_filter = ('is_published', 'created_at', 'category', 'tags', 'author', 'updated_at')
    search_fields = ('title', 'author', 'category', 'tags')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'document', 'is_published', 'created_at', 'updated_at')
    list_filter = ('is_published', 'created_at', 'category', 'tags', 'author', 'updated_at')
    search_fields = ('title', 'author', 'category', 'tags')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)