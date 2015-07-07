from django.conf.urls import patterns, include, url
from django.contrib import admin
from magicblog.views import index, account_profile
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'magicblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^index/$', index),
    (r'^accounts/login/$',  login, {'template_name': 'login.html'}),
    (r'^accounts/logout/$', logout, {'template_name': 'logout.html'}),
    (r'^accounts/profile', account_profile)
)
