from django.shortcuts import render
from rest_framework import views, viewsets
from blog.serializers import *
from blog.models import *

# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer   
    
class LikeBlogViewSet(viewsets.ModelViewSet):
    queryset = LikeBlog.objects.all()
    serializer_class = LikeBlogSerializer 

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer

class ReplyBlogViewSet(viewsets.ModelViewSet):
    queryset = ReplyBlog.objects.all()
    serializer_class = ReplyBlogSerializer
