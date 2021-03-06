from distutils.command.upload import upload
from turtle import textinput
from django.db import models
from django.contrib.auth.models import User
from django.forms import Textarea


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars', null=True, blank=True)
    def __str__(self):
        return f'url: {self.image.url}'

class Userpost(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f'url: {self.image.url}'

class Post(models.Model):
    title = models.CharField(max_length=30)
    sub_title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    content = models.TextField()
    due_date = models.DateField(auto_now=True)
    profile_picture = models.ImageField(upload_to='avatars', null=True, blank=True)
    image_post = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return  self.title


class Ranking(models.Model):
    name_course = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    opinion = models.TextField()
    score = models.IntegerField()
    due_date = models.DateField(auto_now=True)
    profile_picture = models.CharField(max_length=300, null=True, blank=True)
    post_image = models.CharField(max_length=300, null=True, blank=True)
    
    def __str__(self):
        return self.name_course


class Comment(models.Model):
    author = models.CharField(max_length=30)
    text   = models.TextField()
    due_date = models.DateField(auto_now=True)
    post_id = models.IntegerField()

    class Meta:
        ordering = ['-due_date']

class CommentRank(models.Model):
    author = models.CharField(max_length=30)
    text   = models.TextField()
    due_date = models.DateField(auto_now=True)
    rank_id = models.IntegerField()

    class Meta:
        ordering = ['-due_date']

class Message(models.Model):
    author = models.CharField(max_length=30)
    receiver = models.CharField(max_length=30)
    text = models.TextField()
    due_date = models.DateField(auto_now=True)
    profile_picture = models.CharField(max_length=300, null=True, blank=True)
    