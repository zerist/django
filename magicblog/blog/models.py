from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length = 50, unique=True)
    password = models.CharField(max_length = 50)
    is_online = models.BooleanField(default = False)
    email = models.EmailField(unique=True)
    age = models.SmallIntegerField()
    sex = models.CharField(max_length=5, choices=(('man', 'man'), ('woman', 'woman')), default='man')
    city = models.CharField(max_length = 20)
    date = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.username
    
    class Meta:
        ordering = ('age', 'username', 'sex', 'city',)

class Blog(models.Model):
    title = models.CharField(max_length = 60)
    content = models.TextField()
    src = models.URLField()
    author = models.ForeignKey(Account)
    date = models.DateField(auto_now_add=True)
    blog_type = models.CharField(max_length = 20)
    is_transformed = models.BooleanField(default = False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-is_transformed', 'date', 'blog_type', 'author')

class LikeBlog(models.Model):
    like_account = models.ForeignKey(Account)
    like_blog = models.ForeignKey(Blog)
    date = models.DateField(auto_now_add=True)


class Follow(models.Model):
    followe_account = models.ForeignKey(Account)      #something wrong in this 2 line of ForeignKey
    followed_account = models.CharField(max_length = 50)
    date = models.DateField(auto_now_add=True)

class ReplyBlog(models.Model):
    reply_account = models.ForeignKey(Account)
    reply_blog = models.ForeignKey(Blog)
    content = models.CharField(max_length = 280)
    date = models.DateField(auto_now_add=True)



