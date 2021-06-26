from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import slugify

from .models import Post
from profiles.models import UserProfile

from .forms import PostForm
from .forms import CommentForm


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

    # Drafts can only be seen by admin
    if request.user.is_superuser:
        post = get_object_or_404(Post, slug=slug)
    else:
        post = get_object_or_404(Post, slug=slug, status=1)
   
    comment_raw = post.comments.all()
    comments = comment_raw.order_by('-date_added')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        user = UserProfile.objects.get(user=request.user)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = user
            comment.post = post
            comment.comment = request.POST["comment"]
            comment.save()

            messages.success(request, 'Successfully added comment!')
            return redirect('post_detail', slug=post.slug)
    else:
        comment_form = CommentForm()

    template = 'blog/blog_detail.html'
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, template, context)


@login_required
def add_post(request):
    """ Allows admin to add a blog post """

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


@login_required
def edit_post(request, slug):
    """ Allows admin to edit a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save(commit=False)
            slugify(post.title)
            form.save()
            messages.success(request, 'Successfully updated blog post!')
            return redirect(reverse('post_detail', args=[post.slug]))
        else:
            messages.error(request, 'Failed to update blog post. Please ensure the form is valid.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, slug):
    """ Allows admin to delete a blog post """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, slug=slug)
    post.delete()

    messages.success(request, 'Successfully deleted blog post!')
    return redirect(reverse('posts'))
