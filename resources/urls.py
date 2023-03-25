from . import views
from django.urls import path


app_name = 'resources'
urlpatterns = [
    path('', views.article, name='articles'),
    path('videos/', views.video, name='videos'),
    path('documents/', views.documents, name='documents'),
    # path('terms-and-conditions/', views.terms, name='terms'),
    # path('privacy-policy/', views.privacy, name='privacy'),
    # path('faq/', views.faq, name='faq'),
    # path('help/', views.help, name='help'),
    # path('ar/', views.ar, name='help'),
]
