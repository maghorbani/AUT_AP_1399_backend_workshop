from .models import Post, Comment
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# Create your views here.
def index(req):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(req, 'posts/index.html', context=context)

def postDetails(req, id):
    try:
        post = Post.objects.get(pk=id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return render(req, 'posts/details.html', context={ 'post': post })