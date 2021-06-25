from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post


def post(request):
    """ A view to return the blog page """

    posts = Post.objects.filter(status=1)

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)