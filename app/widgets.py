from django.forms import ClearableFileInput
from django.utils.translation import gettext_lazy as _



class MyFileInput(ClearableFileInput):
    clear_checkbox_label = _('Clear')
    initial_text = _('Currently')
    input_text = _('Change')
    template_name = 'app/widgets/my_file_input.html'

    def __init__(self, imgs=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.files = imgs

    def clear_checkbox_name(self, name):
        """
        Given the name of the file input, return the name of the clear checkbox
        input.
        """
        return name + '-clear'

    def clear_checkbox_id(self, name):
        """
        Given the name of the clear checkbox input, return the HTML id for it.
        """
        return name + '_id'

    def is_initial(self, value):
        """
        Return whether value is considered to be initial value.
        """
        return bool(value and getattr(value, 'url', False))


    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget'].update({
            'files': self.files,
        })
        return context
