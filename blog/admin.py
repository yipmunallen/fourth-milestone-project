from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'summary',
        'author',
        'created_on',
        'status',
    )
    list_filter = (
        "status",
    )
    prepopulated_fields = {
        'slug': ('title',)
    }   


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'comment',
        'date_added',
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)