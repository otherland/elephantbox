from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.BlogIndex, name="blog"),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail, name="entry_detail"),
)
