from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('portfolio.views',
    url(r'^accueil/','home'),
    url(r'^contact/','contact'),
    url(r'^user/(\d+)/$','view_user'),
    url(r'^user/all/$','view_all'),
    url(r'^$','tpl')
)
