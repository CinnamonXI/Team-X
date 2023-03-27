from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('terms-and-conditions/', views.terms, name='terms'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('faqs/', views.faq, name='faq'),
    path('faqs/<slug:slug>/', views.faq, name='faqs_category'),
]
