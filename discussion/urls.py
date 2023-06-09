from . import views
from django.urls import path

app_name = 'questions'
urlpatterns=[
    path('', views.questions, name='all'),
    path('ask/', views.ask, name='ask'),
    path('tags/', views.tag_list, name='tags'),
    path('search/', views.search, name='search'),
    path('groups/', views.group_list, name='groups'),
    path('communities/', views.communities, name='communities'),
    path('<slug:slug>/', views.question_detail, name='question_detail'),
    path('groups/<slug:slug>/', views.group_posts, name='group_detail'),
    path('tags/<slug:slug>/', views.follow_unfollow_tag, name='follow_unfollow_tag'),
    path('categories/<slug:slug>/', views.category_detail, name='category_detail'),
    path('communities/<slug:slug>/', views.community_posts, name='community_detail'),
    path('groups/<slug:slug>/about/', views.group_about, name='group_about'),
    path('groups/<slug:slug>/join-leave/', views.join_leave_group, name='join_leave_group'),
    path('ask/community/<slug:slug>', views.ask_community, name='ask_community'),
    path('tags/<slug:slug>/questions/', views.tag_detail, name='tag_detail'),
    path('ask/group/<slug:slug>', views.ask_group, name='ask_group'),
    path('communities/<slug:slug>/about/', views.community_about, name='community_about'),
    path('communities/<slug:slug>/follow-unfollow/', views.follow_unfollow_community, name='follow_unfollow_community'),
    path('answer/<int:answer_id>/like/', views.like_answer, name='like_answer'),
    path('answer/<int:answer_id>/dislike/', views.dislike_answer, name='dislike_answer'),
    path('question/<int:question_id>/like/', views.like_question, name='like_question'),
    path('question/<int:question_id>/dislike/', views.dislike_question, name='dislike_question'),
]