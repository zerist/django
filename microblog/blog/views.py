#-*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from blog.models import *
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.views.generic import View
import nltk
import re
# Create your views here.

def index(request, pk):
    if request.is_ajax():
        blogs = Blog.objects.all()
        json_data = serializers.serialize('json', blogs)
        return HttpResponse(json_data)
    if request.method == 'GET':
        account = Account.objects.get(id=pk)
        return render_to_response('index.html', {'username': account.username})

def showblog(request, account_id, blog_id):
    if request.is_ajax():
        account = Account.objects.get(id=account_id)
        blog = Blog.objects.get(id=blog_id)
        json_data = serializers.serialize('json', [account, blog])
        return HttpResponse(json_data)

    if request.method == 'GET':
        return render_to_response('showblog.html', {})
        

def test(request):
    return render_to_response('test.html')

def category(request, pk):
    if request.is_ajax():
        blogs = Blog.objects.all()
        blog_types = []
        tmp_list = []
        for i in blogs:
            if i.blog_type not in tmp_list:
                tmp_list.append(i.blog_type)
                blog_types.append(i)
        json_data = serializers.serialize('json', blog_types)
        return HttpResponse(json_data)

    if request.method == 'GET':
        account = Account.objects.get(id=pk)
        return render_to_response('category.html', {'username': account.username})

def login(request):
    return render_to_response('login.html')

def logout(request, pk):
    return render_to_response('logout.html', {})

def register(request):
    return render_to_response('register.html', {})

def myself(request, pk):
    account_id = pk
    if account_id:
        account = Account.objects.get(id=account_id)
        username = account.username
        email = account.email
        city = account.city
        age = account.age
        sex = account.sex
    
    return render_to_response('person.html', {
        'username':username,
        'email':email,
        'city':city,
        'age':age,
        'sex':sex
    })


def myblog(request, pk):
    if request.is_ajax():
        account_id = pk
        account = Account.objects.get(id=account_id)
        blogs = Blog.objects.filter(author=account)
        json_data = serializers.serialize('json', blogs)
        return HttpResponse(json_data)
    return render_to_response('myblog.html', {})


class AccountView(View):
    def get(self, request, *args, **kwargs):
        id = re.search('([0-9]+)', request.path).group(0)
        account = Account.objects.get(id=id)
        json_data = serializers.serialize('json', [account])
        return HttpResponse(json_data)
    def put(self, request, *args, **kwargs):
        id = re.search('([0-9]+)', request.path).group(0)
        raw_data = request.body
        data = handle_body(raw_data)
        Account.objects.filter(id=id).update(username=data['username'], password=data['password'], email=data['email'], sex=data['sex'], age=data['age'],
        city=data['city'],is_online=data['is_online'])
        result = Account.objects.get(id=id)
        json_data = serializers.serialize('json', [result])
        return HttpResponse(json_data)

    def patch(self, request, *args, **kwargs):
        id = re.search('([0-9]+)', request.path).group(0)
        raw_data = request.body
        data = handle_body(raw_data)
        account = Account.objects.get(id=id)
        username = data.get('username') or account.username
        password = data.get('password') or account.password
        email = data.get('email') or account.email
        sex = data.get('sex') or account.sex
        age = data.get('age') or account.age
        city = data.get('age') or account.city
        is_online = data.get('is_online', 'none')
        if is_online == 'false':
            is_online = False
        elif is_online == 'true':
            is_online == True;
        elif is_online == 'none':
            is_online == account.is_online
        Account.objects.filter(id=id).update(username=username, password=password, email=email, sex=sex, age=age, city=city, is_online=is_online)
        result = Account.objects.get(id=id)
        json_data = serializers.serialize('json', [result])
        return HttpResponse(json_data)

    def delete(self, request, *args, **kwargs):
        id = re.search('([0-9]+)', request.path).group(0)
        Account.objects.filter(id=id).delete()
        return HttpResponse('')
        


def account(request):
    #get all account values   :    account-list
    if request.method == 'GET' and request.path == '/account/':
        accounts = Account.objects.all()
        json_data = serializers.serialize('json' ,accounts) 
        return HttpResponse(json_data, content_type='application/json')

    #create new account       
    if request.method == 'POST':
        accounts = Account.objects.all()

        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        is_online = request.POST.get('is_online')
        if is_online == 'false':
            is_online = False
        else:
            is_online = True
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
        id = re.search('([0-9]+)', request.path).group(0)
        blog = Blog.objects.get(id=id)
        json_data = serializers.serialize('json', [blog])
        return HttpResponse(json_data)

    def put(self, request, *args, **kwargs):
        id = re.search('([0-9]+)', request.path).group(0)
        raw_data = request.body
        data = handle_body(raw_data)
        author = Account.objects.get(username=data['author'])
        Blog.objects.filter(id=id).update(title=data['title'], content=data['content'], src=data['src'], author=author,blog_type=data['blog_type'], is_transformed=data['is_transformed'])
        result = Blog.objects.get(id=id)
        json_data = serializers.serialize('json', [result])
        return HttpResponse(json_data)

    def patch(self, request, *args, **kwargs):
        id = re.search('([0-9]+)', request.path).group(0)
        blog = Blog.objects.get(id=id)
        data = handle_body(request.body)
        title = data.get('title') or blog.title
        content = data.get('title') or blog.content
        src = data.get('src') or blog.src
        author = data.get('account', '')
        if author == '':
            author = account.author
        else:
            author = Account.objects.get(username=author)
        blog_type = data.get('blog_type') or blog.blog_type
        is_transformed = data.get('is_transformed', 'none')
        if is_transformed == 'false':
            is_transformed = False
        elif is_transformed == 'true':
            is_transformed = True
        elif is_transformed == 'none':
            is_transformed = blog.is_transformed

        Blog.objects.filter(id=id).update(title=title, content=content, src=src, author=author, blog_type=blog_type, is_transformed=is_transformed)
        result = Blog.objects.get(id=id)
        json_data = serializers.serialize('json', [result])
        return HttpResponse(json_data)

    def delete(self, request, *args, **kwargs):
        id = re.search('([0-9]+)', request.path).group(0)
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
        content = request.POST.get('content')
        src = request.POST.get('src')
        author = Account.objects.get(id=request.POST.get('author_id[]'))
        blog_type = request.POST.get('blog_type')
        is_transformed = request.POST.get('is_transformed')

        try:
            data = blogs.create(title=title, content=content, src=src, author=author, blog_type=blog_type, is_transformed=is_transformed)
            json_data = serializers.serialize('json', [data])
            return HttpResponse(json_data)
        except Exception, e:
            return HttpResponse(e)


class LikeBlogView(View):
    def get(self, request, *args, **kwargs):
        id = re.search('([0-9]+)', request.path).group(0)
        likeblog = LikeBlog.objects.get(id=id)
        json_data = serializers.serialize('json', [likeblog])
        return HttpResponse(json_data)

    def put(self, request, *args, **kwargs):
        id = re.search('([0-9]+)', request.path).group(0)

        data = handle_body(request.body)
        account = Account.objects.get(username=data['author'])
        blog = Blog.objects.get(id=data['blog_id'])

        LikeBlog.objects.filter(id=id).update(like_account=account, like_blog=blog)
        result = LikeBlog.objects.get(id=id)
        json_data = serializers.serialize('json', [result])
        return HttpResponse(json_data)

    def patch(self, request, *args, **kwargs):
        id = re.search('([0-9]+)', request.path).group(0)
        likeblog = LikeBlog.objects.get(id=id)

        data = handle_body(request.body)
        account = data.get('author', '')
        if account == '':
            account = likeblog.like_account
        else:
            account = Account.objects.get(username=account)
        blog = data.get('blog', '')
        if blog == '':
            blog = likeblog.like_blog
        else:
            blog = Blog.objects.get(id=blog)


        LikeBlog.objects.filter(id=id).update(like_account=account, like_blog=blog)
        result = LikeBlog.objects.get(id=id)
        json_data = serializers.serialize('json', [result])
        return HttpResponse(json_data)

    def delete(self, request, *args, **kwargs):
        id = re.search('([0-9]+)', request.path).group(0)
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
        blog = Blog.objects.get(id=request.POST.get('blog_id[]'))

        try:
            data = likeblogs.create(like_account=account, like_blog=blog)
            json_data = serializers.serialize('json', [data])
            return HttpResponse(json_data)
        except:
            return HttpResponse('wrong data')


class FollowView(View):
    def get(self, request, *args, **kwargs):
        id = re.search('([0-9]+)', request.path).group(0)
        follow = Follow.objects.get(id=id)
        json_data = serializers.serialize('json', [follow])
        return HttpResponse(json_data)

    def put(self, request, *args, **kwargs):
        id = re.search('([0-9]+)', request.path).group(0)
        data = handle_body(request.body)
        followe_account = Account.objects.get(username=data['follow_account'])
        followed_account = data['followed_account']

        Follow.objects.filter(id=id).update(followe_account=followe_account, followed_account=followed_account)
        result = Follow.objects.get(id=id)
        json_data = serializers.serialize('json', [result])
        return HttpResponse(json_data)

    def patch(self, request, *args, **kwargs):
        id = re.search('([0-9]+)', request.path).group(0)
        follow = Follow.objects.get(id=id)
        data = handle_body(request.body)
        followe_account = data.get('follow_account', '')
        if followe_account == '':
            followe_account = follow.followe_account
        else:
            followe_account = Account.objects.get(username=followe_account)
        followed_account = data.get('followed_account') or follow.followed_account

        Follow.objects.filter(id=id).update(followe_account=followe_account, followed_account=followed_account)
        result = Follow.objects.get(id=id)
        json_data = serializers.serialize('json', [result])
        return HttpResponse(json_data)

    def delete(self, request, *args, **kwargs):
        id = re.search('([0-9]+)', request.path).group(0)
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
            followe_account = Account.objects.get(id=request.POST.get('follow_account[]'))

            try:
                data = followblogs.create(followe_account=followe_account, followed_account=followed_account)
                json_data = serializers.serialize('json', [data])
                return HttpResponse(json_data)
            except:
                return HttpResponse('wrong data')

class ReplyBlogView(View):
    def get(self, request, *args, **kwargs):
        id = re.search('([0-9]+)', request.path).group(0)
        reply = ReplyBlog.objects.get(id=id)
        json_data = serializers.serialize('json', [reply])
        return HttpResponse(json_data)

    def put(self, request, *args, **kwargs):
        id = re.search('([0-9]+)', request.path).group(0)
        data = handle_body(request.body)
        reply_account = Account.objects.get(username=data['reply_account'])
        reply_blog = Blog.objects.get(id=data['reply_blog'])
        content = data['content']

        ReplyBlog.objects.filter(id=id).update(reply_account=reply_account, reply_blog=reply_blog, content=content)
        result = ReplyBlog.objects.get(id=id)
        json_data = serializers.serialize('json', [result])
        return HttpResponse(json_data)

    def patch(self, request, *args, **kwargs):
        id = re.search('([0-9]+)', request.path).group(0)
        reply = ReplyBlog.objects.get(id=id)
        data = handle_body(request.body)
        reply_account = data.get('reply_account', '')
        if reply_account == '':
            reply_account = reply.reply_account
        else:
            reply_account = Account.objects.get(username=reply_account)
        reply_blog = data.get('reply_blog', '')
        if reply_blog == '':
            reply_blog = reply.reply_blog
        else:
            reply_blog = Blog.objects.get(id=reply_blog)
        content = data.get('content') or reply.content

        ReplyBlog.objects.filter(id=id).update(reply_account=reply_account, reply_blog=reply_blog, content=content)
        result = ReplyBlog.objects.get(id=id)
        json_data = serializers.serialize('json', [result])
        return HttpResponse(json_data)

    def delete(self, request, *args, **kwargs):
        iid = re.search('([0-9]+)', request.path).group(0)
        ReplyBlog.objects.filter(id=id).delete()
        return HttpResponse('')

def replyblog(request):
    if request.method == 'GET':
        replyblogs = ReplyBlog.objects.all()
        json_data = serializers.serialize('json', replyblogs)
        return HttpResponse(json_data)

    if request.method == 'POST':
        replyblogs = ReplyBlog.objects.all()

        reply_account = Account.objects.get(id=request.POST.get('reply_account'))
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
