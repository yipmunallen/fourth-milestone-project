from django import forms
from products.widgets import CustomClearableFileInput

from .models import Post
from .models import Comment


class PostForm(forms.ModelForm):
    """ A form for admin to add or edit blog posts """

    class Meta:
        model = Post
        exclude = ('slug',)

    image = forms.ImageField(label='Image', required=True, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
  
        self.fields['title'].widget.attrs['autofocus'] = True


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comment'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs['placeholder'] = 'Write your comment here...'