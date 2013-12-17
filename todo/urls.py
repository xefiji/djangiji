#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView,ListView
from todo.models import Todo
from todo.views import ListTodos
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('todo.views',
                       # url(r'^$','home'),
                       url(r'^$',login_required(ListTodos.as_view()),name='home'),
                       url(r'^add','add'),
                       url(r'^contact','contact'),
                       url(r'^remove/(\d+)','remove'),
                       url(r'^toggle/(\d+)','toggle'),
                       url(r'^save/(\d+)','save'),
                       url(r'^login','cnx'),

                       url(r'^logout','cnx_out'),
                       url(r'^faq/$',TemplateView.as_view(template_name='todo/faq.html'),{'page_title':"Faq"}),
                       )

urlpatterns += patterns('',
                        url(r'^renew','django.contrib.auth.views.password_change',{'template_name': 'todo/renew.html', 'post_change_redirect': '/todo/password_change_done'}),
                        url(r'^password_change_done','django.contrib.auth.views.password_change_done',{'template_name': 'todo/password_change_done.html'}),


                        url(r'^password_reset/$','django.contrib.auth.views.password_reset',{'email_template_name':'todo/password_email.html','post_reset_redirect': '/todo/password_reset_done'}),

                        url(r'^password_reset_done/$','django.contrib.auth.views.password_reset_done',{'template_name': 'todo/password_reset_done.html'}),

                        url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$','django.contrib.auth.views.password_reset_confirm',{'post_reset_redirect': '/todo/password_reset_complete'}),

                        url(r'^password_reset_complete/$','django.contrib.auth.views.password_reset_complete',{'template_name': 'todo/password_reset_complete.html'}),
                        )
