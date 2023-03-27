from django.contrib import admin
from .models import Profile, Team
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('user__username', 'user__email', 'slug')
    prepopulated_fields = {'slug': ('user',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'is_active', 'order', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('title',)
    date_hierarchy = 'created_at'
    ordering = ('order',)