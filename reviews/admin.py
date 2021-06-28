from django.contrib import admin
from .models import Review, Comment


class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'product',
        'user',
        'would_recommend',
        'date_created'
    )


class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'comment',
        'post',
        'date_added',
    )


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
