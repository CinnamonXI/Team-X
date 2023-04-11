from django.contrib import admin
from .models import Community, Group, Question, Answer, AnswerLike
# Register your models here.

@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('title','community', 'group_icon', 'cover_image', 'created_at', 'updated_at')
    list_filter = ('created_at', 'community', 'updated_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'user', 'community', 'group', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'user', 'community', 'group')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'user', 'likes', 'dislikes', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('content', 'question')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

@admin.register(AnswerLike)
class AnswerLikeAdmin(admin.ModelAdmin):
    list_display = ('answer', 'user', 'value')
    # list_filter = ('created_at',)
    search_fields = ('answer', 'user')
    # ordering = ('-created_at',)
    # date_hierarchy = 'created_at'