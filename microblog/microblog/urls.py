from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'microblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', index, name='index'),
    #url(r'^test/(?P<pk>[0-9]+)/$', TestView.as_view(), name='test'),
    url(r'^account/$', account, name='account'),
    url(r'^account/(?P<pk>[0-9]+)/$', AccountView.as_view(), name="account-detail"),
    url(r'^blog/$', blog, name='blog'),
    url(r'^blog/(?P<pk>[0-9]+)/$', BlogView.as_view(), name="blog-detail"),
    url(r'^likeblog/$', likeblog, name='likeblog'),
    url(r'^likeblog/(?P<pk>[0-9]+)/$', LikeBlogView.as_view(), name='likeblog-detail'),
    url(r'^follow/$', follow, name='follow'),
    url(r'^follow/(?P<pk>[0-9]+)/$', FollowView.as_view(), name='follow-detail'),
    url(r'^replyblog/$', replyblog, name='replyblog'),
    url(r'^replyblog/(?P<pk>[0-9]+)/$', ReplyBlogView.as_view(), name="replyblog-detail"),
)
