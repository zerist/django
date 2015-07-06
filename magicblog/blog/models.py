from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length = 50, unique=True)
    password = models.CharField(max_length = 50)
    email = models.EmailField(unique=True)
    age = models.SmallIntegerField()
    sex = models.BooleanField(default = True)
    city = models.CharField(max_length = 20)
    date = models.DateField()

    def __unicode__(self):
        return username

class Blog(models.Model):
    title = models.CharField(max_length = 60)
    content = models.TextField()
    src = models.URLField()
    author = models.ForeignKey(Account)
    date = models.DateField()
    blog_type = models.CharField(max_length = 20)
    is_transfromed = models.BooleanField(default = False)

    def __unicode__(self):
        return title

class LikeBolg(models.Model):
    like_account = models.ForeignKey(Account)
    like_blog = models.ForeignKey(Blog)
    date = models.DateField()


class Follow(models.Model):
    followe_account = models.ForeignKey(Account)      #something wrong in this 2 line of ForeignKey
    followed_account = models.CharField(max_length = 50)
    date = models.DateField()

class ReplyBolg(models.Model):
    reply_account = models.ForeignKey(Account)
    reply_blog = models.ForeignKey(Blog)
    content = models.CharField(max_length = 280)
    date = models.DateField()



