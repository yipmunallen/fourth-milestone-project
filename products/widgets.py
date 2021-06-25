from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'


class CustomClearableFileInput2(ClearableFileInput):
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input_2.html'