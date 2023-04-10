from . import views
from django.urls import path

app_name = 'questions'
urlpatterns=[
    path('', views.questions, name='all'),
    path('ask/', views.ask, name='ask'),
    path('ask/group/<slug:slug>', views.ask_group, name='ask_group'),
    path('ask/community/<slug:slug>', views.ask_community, name='ask_community'),
    path('tags/', views.tag_list, name='tags'),
    path('search/', views.search, name='search'),
    path('groups/', views.group_list, name='groups'),
    path('communities/', views.communities, name='communities'),
    path('<slug:slug>/', views.question_detail, name='question_detail'),
    path('groups/<slug:slug>/', views.group_posts, name='group_detail'),
    path('groups/<slug:slug>/about/', views.group_about, name='group_about'),
    path('groups/<slug:slug>/join-leave/', views.join_leave_group, name='join_leave_group'),
    path('tags/<slug:slug>/', views.follow_unfollow_tag, name='follow_unfollow_tag'),
    path('tags/<slug:slug>/questions/', views.tag_detail, name='tag_detail'),
    path('communities/<slug:slug>/', views.community_posts, name='community_detail'),
    path('communities/<slug:slug>/about/', views.community_about, name='community_about'),
    path('communities/<slug:slug>/follow-unfollow/', views.follow_unfollow_community, name='follow_unfollow_community'),
    path('categories/<slug:slug>/', views.category_detail, name='category_detail'),
]