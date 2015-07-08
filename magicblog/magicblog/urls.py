from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'blog', BlogViewSet)
router.register(r'likeblog', LikeBlogViewSet)
router.register(r'follow', FollowViewSet)
router.register(r'replyblog', ReplyBlogViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'magicblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
)

urlpatterns += router.urls
