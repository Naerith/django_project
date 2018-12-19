from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model): #.Model ne için?
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) #auto_now=True sets time to the last uptade, auto_now_add=True sets time to the first
    #date which post has posted
    author = models.ForeignKey(User, on_delete = models.CASCADE) # ForeignKey makes one post has only one author and an author can have more than one posts
    # on_delete part: if a user is deleted, post will be deleted too.

    def __str__(self): #we tell it to be more descriptive
        return self.title
