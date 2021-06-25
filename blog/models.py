from django.db import models

from profiles.models import UserProfile


class Post(models.Model):
    """
    A blog model that allows admin users to create Blog posts
    """

    STATUS = (
        (0, "Draft"),
        (1, "Publish")
    )

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=60)
    summary = models.TextField(max_length=300)
    content = models.TextField()
    image = models.ImageField(default='')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    A blog model that allows users to comment on blog posts
    """

    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.user)
