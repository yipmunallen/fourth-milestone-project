from django import forms
from .widgets import CustomClearableFileInput
from .widgets import CustomClearableFileInput2
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image 1', required=True, widget=CustomClearableFileInput)
    image_2 = forms.ImageField(label='Image 2', required=True, widget=CustomClearableFileInput2)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'