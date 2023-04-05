from . import views
from django.urls import path

app_name = 'questions'
urlpatterns=[
    # path('', views.all_questions, name='all'),
    path('ask', views.ask, name='ask'),
    
]