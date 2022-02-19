from django import forms
from .models import Article, Mobile, Web, Library

class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # initial = None
        # if 'instance' in kwargs:
            # initial = kwargs['instance'].images.all()
            # populating field ...
            # Note : this dont work because
            # HTML file input fields are never populated with existing data - this is a browser restriction, nothing to do with Django.
            # It's a security measure, to stop malicious sites tricking you into uploading arbitrary content from your computer.
        self.fields['images_list'] = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        fields = '__all__'


class ArticleForm(ProjectForm):

    class Meta(ProjectForm.Meta):
        model = Article


class LibraryForm(ProjectForm):

    class Meta(ProjectForm.Meta):
        model = Library


class MobileForm(ProjectForm):

    class Meta(ProjectForm.Meta):
        model = Mobile


class WebForm(ProjectForm):

    class Meta(ProjectForm.Meta):
        model = Web
