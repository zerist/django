from django.shortcuts import render, render_to_response
from blog.models import *
import json
from django.http import HttpResponse
from django.core import serializers
from django.views.generic import View
import nltk
# Create your views here.

def index(request):
    if request.method == 'GET':
        return render_to_response('index.html', {})



class AccountView(View):
    def get(self, request, *args, **kwargs):
        id = request.path[9:-1]
        account = Account.objects.get(id=id)
        json_data = serializers.serialize('json', [account])
        return HttpResponse(json_data)
    def put(self, request, *args, **kwargs):
        id = request.path[9:-1]
        raw_data = request.body
        data = handle_body(raw_data)
        Account.objects.filter(id=id).update(username=data['username'], password=data['password'], email=data['email'], sex=data['sex'], age=data['age'],
        city=data['city'],is_online=data['is_online'])
        result = Account.objects.get(id=id)
        json_data = serializers.serialize('json', [result])
        return HttpResponse(json_data)

    def patch(self, request, *args, **kwargs):
        id = request.path[9:-1]
        raw_data = request.body
        data = handle_body(raw_data)
        account = Account.objects.get(id=id)
        Account.objects.filter(id=id).update(username=data['username'] or account.username, password=data['password'] or account.password,
        email=data['email'] or account.email, sex=data['sex'] or account.sex, age=data['age'] or account.age, city=data['city'] or account.city, is_online=data['is_online'] or account.is_online)
        result = Account.objects.get(id=id)
        json_data = serializers.serialize('json', [result])
        return HttpResponse(json_data)

    def delete(self, request, *args, **kwargs):
        id = request.path[9:-1]
        Account.objects.filter(id=id).delete()
        return HttpResponse('')
        


def account(request):
    #get all account values   :    account-list
    if request.method == 'GET' and request.path == '/account/':
        accounts = Account.objects.all()
        json_data = serializers.serialize('json' ,accounts) 
        return HttpResponse(json_data)

    #create new account       
    if request.method == 'POST':
        accounts = Account.objects.all()

        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        is_online = request.POST.get('is_online')
        city = request.POST.get('city')
        
        try:
            data = accounts.create(username=username, password=password, email = email, sex=sex, age=age, is_online=is_online, city=city)

            json_data = serializers.serialize('json', [data])
            return HttpResponse(json_data)
        except:
            return HttpResponse('wrong data')


class BlogView(View):
    #get for blog-detail:
    def get(self, request, *args, **kwargs):
        id = request.path[6:-1]
        blog = Blog.objects.get(id=id)
        json_data = serializers.serialize('json', [blog])
        return HttpResponse(json_data)

    def put(self, request, *args, **kwargs):
        id = request.path[6:-1]
        raw_data = request.body
        data = handle_body(raw_data)
        author = Account.objects.get(username=data['author'])
        Blog.objects.filter(id=id).update(title=data['title'], content=data['content'], src=data['src'], author=author,blog_type=data['blog_type'], is_transformed=data['is_transformed'])
        result = Blog.objects.get(id=id)
        json_data = serializers.serialize('json', [result])
        return HttpResponse(json_data)

    def patch(self, request, *args, **kwargs):
        id = request.path[6:-1]
        blog = Blog.objects.get(id=id)
        data = handle_body(request.body)
        title = data['title'] or blog.title
        content = data['title'] or blog.content
        src = data['src'] or blog.src
        author = Account.objects.get(username=data['author']) or blog.author
        blog_type = data['blog_type'] or blog.blog_type
        is_transformed = data['is_transformed'] or blog.is_transformed

        Blog.objects.filter(id=id).update(title=title, content=content, src=src, author=author, blog_type=blog_type, is_transformed=is_transformed)
        result = Blog.objects.get(id=id)
        json_data = serializers.serialize('json', [result])
        return HttpResponse(json_data)

    def delete(self, request, *args, **kwargs):
        id = request.path[6:-1]
        Blog.objects.filter(id=id).delete()
        return HttpResponse('')



def blog(request):
    #get all blog values    :       blog-list
    if request.method == 'GET':
        blogs = Blog.objects.all()
        json_data = serializers.serialize('json', blogs)
        return HttpResponse(json_data)

    #post  for create new blog
    if request.method == 'POST':
        blogs = Blog.objects.all()
        title = request.POST.get('title')
        content = request.POST.get('title')
        src = request.POST.get('src')
        author = Account.objects.get(username=request.POST.get('author'))
        blog_type = request.POST.get('blog_type')
        is_transformed = request.POST.get('is_transformed')

        try:
            data = blogs.create(title=title, content=content, src=src, author=author, blog_type=blog_type, is_transformed=is_transformed)
            json_data = serializers.serialize('json', [data])
            return HttpResponse(json_data)
        except:
            return HttpResponse('wrong data')


class LikeBlogView(View):
    def get(self, request, *args, **kwargs):
        id = request.path[10:-1]
        likeblog = LikeBlog.objects.get(id=id)
        json_data = serializers.serialize('json', [likeblog])
        return HttpResponse(json_data)

    def put(self, request, *args, **kwargs):
        id = request.path[10:-1]

        data = handle_body(request.body)
        account = Account.objects.get(username=data['author'])
        blog = Blog.objects.get(id=data['blog_id'])

        LikeBlog.objects.filter(id=id).update(like_account=account, like_blog=blog)
        result = LikeBlog.objects.get(id=id)
        json_data = serializers.serialize('json', [result])
        return HttpResponse(json_data)

    def patch(self, request, *args, **kwargs):
        id = request.path[10:-1]
        likeblog = LikeBlog.objects.get(id=id)

        data = handle_body(request.body)
        account = Account.objects.get(username=data['author']) or likeblog.like_account
        blog = Blog.objects.get(id=data['blog_id']) or likeblog.like_blog

        LikeBlog.objects.filter(id=id).update(like_account=account, like_blog=blog)
        result = LikeBlog.objects.get(id=id)
        json_data = serializers.serialize('json', [result])
        return HttpResponse(json_data)

    def delete(self, request, *args, **kwargs):
        id = request.path[10:-1]
        LikeBlog.objects.filter(id=id).delete()
        return HttpResponse('')


def likeblog(request):
    if request.method == 'GET':
        likeblogs = LikeBlog.objects.all()
        json_data = serializers.serialize('json', likeblogs)
        return HttpResponse(json_data)

    if request.method == 'POST':
        likeblogs = LikeBlog.objects.all()

        account = Account.objects.get(username=request.POST.get('author'))
        blog = Blog.objects.get(id=request.POST.get('blog_id'))

        try:
            data = likeblogs.create(like_account=account, like_blog=blog)
            json_data = serializers.serialize('json', [data])
            return HttpResponse(json_data)
        except:
            return HttpResponse('wrong data')


class FollowView(View):
    def get(self, request, *args, **kwargs):
        id = request.path[8:-1]
        follow = Follow.objects.get(id=id)
        json_data = serializers.serialize('json', [follow])
        return HttpResponse(json_data)

    def put(self, request, *args, **kwargs):
        id = request.path[8:-1]

        data = handle_body(request.body)
        followe_account = Account.objects.get(username=data['follow_account'])
        followed_account = data['followed_account']

        Follow.objects.filter(id=id).update(followe_account=followe_account, followed_account=followed_account)
        result = Follow.objects.get(id=id)
        json_data = serializers.serialize('json', [result])
        return HttpResponse(json_data)

    def patch(self, request, *args, **kwargs):
        id = request.path[8:-1]
        follow = Follow.objects.get(id=id)
        data = handle_body(request.body)
        followe_account = Account.objects.get(username=data['follow_account']) or follow.followe_account
        followed_account = data['followed_account'] or follow.followed_account

        Follow.objects.filter(id=id).update(followe_account=followe_account, followed_account=followed_account)
        result = Follow.objects.get(id=id)
        json_data = serializers.serialize('json', [result])
        return HttpResponse(json_data)

    def delete(self, request, *args, **kwargs):
        id = request.path[8:-1]
        Follow.objects.filter(id=id).delete()
        return HttpResponse('')

def follow(request):
    if request.method == 'GET':
            followblogs = Follow.objects.all()
            json_data = serializers.serialize('json', followblogs)
            return HttpResponse(json_data)

    if request.method == 'POST':
            followblogs = Follow.objects.all()
        
            followed_account = request.POST.get('followed_account')
            followe_account = Account.objects.get(username=request.POST.get('follow_account'))

            try:
                data = followblogs.create(followe_account=followe_account, followed_account=followed_account)
                json_data = serializers.serialize('json', [data])
                return HttpResponse(json_data)
            except:
                return HttpResponse('wrong data')

class ReplyBlogView(View):
    def get(self, request, *args, **kwargs):
        id = request.path[11:-1]
        reply = ReplyBlog.objects.get(id=id)
        json_data = serializers.serialize('json', [reply])
        return HttpResponse(json_data)

    def put(self, request, *args, **kwargs):
        id = request.path[11:-1]

        data = handle_body(request.body)
        reply_account = Account.objects.get(username=data['reply_account'])
        reply_blog = Blog.objects.get(id=data['reply_blog'])
        content = data['content']

        ReplyBlog.objects.filter(id=id).update(reply_account=reply_account, reply_blog=reply_blog, content=content)
        result = ReplyBlog.objects.get(id=id)
        json_data = serializers.serialize('json', [result])
        return HttpResponse(json_data)

    def patch(self, request, *args, **kwargs):
        id = request.path[11:-1]
        reply = ReplyBlog.objects.get(id=id)
        data = handle_body(request.body)
        reply_account = Account.objects.get(username=data['reply_account']) or reply.reply_account
        reply_blog = Blog.objects.get(id=data['reply_blog']) or reply.reply_blog
        content = data['content'] or reply.content

        ReplyBlog.objects.filter(id=id).update(reply_account=reply_account, reply_blog=reply_blog, content=content)
        result = ReplyBlog.objects.get(id=id)
        json_data = serializers.serialize('json', [result])
        return HttpResponse(json_data)

    def delete(self, request, *args, **kwargs):
        id = request.path[11:-1]
        ReplyBlog.objects.filter(id=id).delete()
        return HttpResponse('')

def replyblog(request):
    if request.method == 'GET':
        replyblogs = ReplyBlog.objects.all()
        json_data = serializers.serialize('json', replyblogs)
        return HttpResponse(json_data)

    if request.method == 'POST':
        replyblogs = ReplyBlog.objects.all()

        reply_account = Account.objects.get(username=request.POST.get('reply_account'))
        reply_blog = Blog.objects.get(id=request.POST.get('reply_blog'))
        content = request.POST.get('content')

        try:
            data = replyblogs.create(reply_account=reply_account, reply_blog=reply_blog, content=content)
            json_data = serializers.serialize('json', [data])
            return HttpResponse(json_data)
        except:
            return HttpResponse('wrong data')

def handle_body(raw_data):
    data = {}
    tokens = nltk.word_tokenize(raw_data)
    for i in range(len(tokens)-1):
        if tokens[i] == 'name=':
            data[tokens[i+2]] = tokens[i+4]

    return data
