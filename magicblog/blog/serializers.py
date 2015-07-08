from rest_framework import serializers
from blog.models import *

class AccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Account

class BlogSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = Blog
 
class LikeBlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LikeBlog     
        
class FollowSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Follow  

class ReplyBlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ReplyBlog
