# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('is_online', models.BooleanField(default=False)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('age', models.SmallIntegerField()),
                ('sex', models.CharField(default=b'man', max_length=5, choices=[(b'man', b'man'), (b'woman', b'woman')])),
                ('city', models.CharField(max_length=20)),
                ('date', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ('age', 'username', 'sex', 'city'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('content', models.TextField()),
                ('src', models.URLField()),
                ('date', models.DateField(auto_now_add=True)),
                ('blog_type', models.CharField(max_length=20)),
                ('is_transformed', models.BooleanField(default=False)),
                ('author', models.ForeignKey(to='blog.Account')),
            ],
            options={
                'ordering': ('-is_transformed', 'date', 'blog_type', 'author'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('followed_account', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('followe_account', models.ForeignKey(to='blog.Account')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LikeBlog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('like_account', models.ForeignKey(to='blog.Account')),
                ('like_blog', models.ForeignKey(to='blog.Blog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReplyBlog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=280)),
                ('date', models.DateField(auto_now_add=True)),
                ('reply_account', models.ForeignKey(to='blog.Account')),
                ('reply_blog', models.ForeignKey(to='blog.Blog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
