from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars', null=True, blank=True)
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



