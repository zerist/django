from django.conf.urls import patterns, include, url
from django.contrib import admin
from magicblog.views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'magicblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^index/$', index),
)
