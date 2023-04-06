from . import views
from django.urls import path

app_name = 'questions'
urlpatterns=[
    path('', views.all_questions, name='all'),
    path('unanswered/', views.unanswered, name='unanswered'),
    path('most-answered/', views.most_answered, name='most-answered'),
    path('most-recent/', views.most_recent, name='most-recent'),
    path('ask/', views.ask, name='ask'),
    path('groups/', views.group_list, name='groups'),
    path('tags/', views.tag_list, name='tags'),
    path('badges/', views.badge_list, name='badges'),
    path('communities/', views.communities, name='communities'),
    path('communities/<slug:slug>/', views.community_detail, name='community_detail'),
    path('communities/<slug:slug>/follow-unfollow/', views.follow_unfollow_community, name='follow_unfollow_community'),
]