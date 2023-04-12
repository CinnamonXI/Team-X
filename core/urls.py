from . import views
from django.urls import path
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('', views.index, name='index'),
    path(_('search/'), views.search, name='search'),
    path(_('about/'), views.about, name='about'),
    path(_('contact/'), views.contact, name='contact'),
    path(_('terms-and-conditions/'), views.terms, name='terms'),
    path(_('privacy-policy/'), views.privacy, name='privacy'),
    path(_('faqs/'), views.faq, name='faq'),
    path('faqs/<slug:slug>/', views.faq, name='faqs_category'),
]
