from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
   {
   'title':'this is a quo',
   'quo':'How do you tell a Communist? Well, its someone who reads Marx and Lenin. And how do you tell an anti-Communist? Its someone who understands Marx and Lenin.',
   'owner':'ronald reagan'
   },
   {
   'title':'this is not a quo',
   'quo':'kzklr',
   'owner':'tols'
   },
]

def home(request):
    dict = {
    "postss": Post.objects.all() #it makes the posts as the ones which we produced in terminal
    #posts #second posts has the data of our posts
    }
    return render(request, 'blog/home.html', dict)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
