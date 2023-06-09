from . import views
from django.urls import path


app_name = 'resources'
urlpatterns = [
    path('', views.article, name='articles'),
    path('category/<slug:slug>/', views.article, name='articles_category'),
    path('articles/<slug:slug>/', views.article_details, name='article_details'),
    path('articles/tags/<slug:slug>/', views.article_tags, name='article_tags'),
    #Videos
    path('videos/', views.video, name='videos'),
    path('videos/<slug:slug>/', views.video, name='videos_category'),
    path('videos/tags/<slug:slug>/', views.video_tags, name='video_tags'),
    #Documents
    path('documents/', views.documents, name='documents'),
    path('documents/<slug:slug>/', views.documents, name='documents_category'),
]
