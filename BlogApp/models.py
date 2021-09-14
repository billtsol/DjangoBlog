from django.db import models
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Author(models.Model):
    author = models.ForeignKey(User,on_delete=models.PROTECT)
    username = models.CharField(max_length=50)
    image = models.ImageField(upload_to='users')
    created = models.DateTimeField(auto_now_add=True)
    specialty = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=40)
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category')
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='post')
    desc = models.TextField()
    body = RichTextField()
    author = models.ForeignKey(Author,on_delete=models.PROTECT)
    category = models.ManyToManyField(Category)
    commentCount = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    commentPost = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user = models.CharField(max_length=255)
    comment = models.TextField(max_length=512)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user