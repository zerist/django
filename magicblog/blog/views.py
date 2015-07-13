import exceptions
from django.shortcuts import render, render_to_response
from rest_framework import views, viewsets, status
from rest_framework.response import Response
from blog.serializers import *
from blog.models import *
from lib import tools

# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class LoginView(views.APIView):
    def get(self, request, format=None):
        return render_to_response('login.html', {})

    def post(self, request, format=None):
        if request.POST.has_key('login'):
            if request.POST.get('id'):
                return render_to_response('index.html', {})
            else:
                return render_to_response('login.html', {'message_username': 'wrong username or password'})
        

class UserView(views.APIView):
    message = {'username':'', 'password':''}

    def get(self, request, format=None):
        return render_to_response('login.html', {}) 

    def post(self, request, format=None):
        serializer = AccountSerializer(data = request.data)
        try:
            is_login = request.POST['login']
            
            if is_login == "login":
                post_username = serializer.initial_data['username']
                post_password = serializer.initial_data['password']
        
                try:
                    account = Account.objects.get(username=post_username)
                except exceptions.Exception, e:
                    self.message['username'] = 'No Such Account'
                    return render_to_response('login.html', {'message_username':self.message['username']}) 
        
                if post_password == account.password:
                    
                    return render_to_response('index.html', {})
                else:
                    self.message['password'] = 'wrong password for this account'
                    return render_to_response('login.html', {'message_password':self.message['password']})

        except:
            message = {}
            
            if serializer.initial_data.get('register', ''):
                return render_to_response('register.html', {})
            if serializer.initial_data.get('cancel', ''):
                return render_to_response('login.html', {})
            if serializer.initial_data.get('confirm', ''):
                username = serializer.initial_data.get('re_username', '')
                password = serializer.initial_data.get('re_password', '')
                confirm_password = serializer.initial_data.get('confirm_password', '')
                email = serializer.initial_data.get('email', '')
                age = serializer.initial_data.get('age', '')
                sex = serializer.initial_data.get('sex', '')
                city = serializer.initial_data.get('city', '')

                if not username or len(username) > 50:
                    message['username'] = "username should not be empty or longer than 50 characters"
                elif not password or len(password) > 50:
                    message['password'] = "password should not be empty or longer than 50 characters"
                elif password != confirm_password:
                    message['confirm_password'] = "not equal with password above"
                elif not email or email.find('@') == -1:
                    message['email'] = "email should not be empty or wrong email address"
                elif not age:
                    message['age'] = "age should not be empty"
                elif not city or len(city) > 20:
                    message['city'] = 'city should not be empty or longer than 20 charactersa'
                else:
                    data = {'username':username, 'password':password, 'email':email, 'city':city, 'sex':sex, 'age':age}
                    tools.http_post('accounts/', data)
                    return render_to_response('login.html', {'message_success': 'Create User Successful! Now You Can Login'}) 
                    
                        
            return render_to_response('register.html', {'message': message})
        
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


