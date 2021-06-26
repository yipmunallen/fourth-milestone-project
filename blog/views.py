from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify

from .models import Post

from .forms import PostForm


def all_posts(request):
    """ A view to return the blog page """

    if request.user.is_authenticated and request.user.is_superuser:
        posts = Post.objects.all()
    else:
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


@login_required
def add_post(request):
    """ A view that allows admin to add a blog post """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post = form.save()
            messages.success(request, 'Successfully added a blog post!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, 'Failed to add the blog post. Please ensure the form is valid.')
    else:
        form = PostForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
