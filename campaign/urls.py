from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^care/$', views.care, name='care'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^giving/$', views.giving, name='giving'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^shop/$', views.shop, name='shop'),
]
