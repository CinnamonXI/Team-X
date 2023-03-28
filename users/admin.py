from django.contrib import admin
from .models import Profile, Team, Follower
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'gender', 'phone_number', 'created_at', 'updated_at')
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

@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('user_from', 'user_to', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user_from','user_to')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'