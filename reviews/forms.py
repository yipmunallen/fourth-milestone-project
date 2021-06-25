from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """ A form for users to add a review to a product """

    class Meta:
        model = Review
        exclude = (
            'user',
            'date_created',
            'product')

        fields = [
            'title',
            'description',
            'rating',
            'would_recommend']

        labels = {
            'would_recommend': 'I would recommend this product',
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders for the review form
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'description': 'Write your review here...',
        }

        # Add placeholders and classes to input fields
        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'rating' and field != 'would_recommend':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False
