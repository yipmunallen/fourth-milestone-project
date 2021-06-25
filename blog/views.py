from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post


def all_posts(request):
    """ A view to return the blog page """

    posts = Post.objects.filter(status=1)

    template = 'blog/blog.html'
    context = {
        'posts': posts,
    }

    return render(request, template, context)


def post_detail(request, slug):
    """ A view to return a blog post page """

    post = Post.objects.get(slug=slug)

    template = 'blog/blog_detail.html'
    context = {
        'post': post,
    }

    return render(request, template, context)
