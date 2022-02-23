from django import forms
from django.utils.translation import gettext_lazy as _
from parler.forms import TranslatableModelFormMixin, TranslatableModelFormMetaclass
from .models import Article, Application, Library, ContactMessage
from .widgets import  MyFileInput



class ContactMessageForm(forms.ModelForm):

    class Meta:
        model = ContactMessage
        fields = ('sender_mail', 'sender_phone', 'full_name', 'content')
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder':'',
                                                'autocomplete': 'off',
                                                'class': 'latter-control',
                                                }),
            'sender_phone': forms.TextInput(attrs={'placeholder':'',
                                                    'class': 'latter-control',
                                                    'autocomplete': 'off',
                                                }),
            'sender_mail' : forms.EmailInput(attrs={'placeholder':'',
                                                    'class': 'latter-control',
                                                    'autocomplete': 'off',
                                                }),
            'content' : forms.Textarea(attrs={'placeholder':'',
                                                    'class': 'latter-control',
                                                    'rows': 3,
                                                    'cols': 25,
                                                }),
        }
        labels = {

        }
        error_messages = {
            'full_name': {
                'max_length': "تعداد کاراکترها بیش از حد مجاز هست",
                'required': 'این فیلد نباید خالی باشد',
                'unique': "کاربری با این نام از قبل وجود دارد",
            },
            'content': {
                'max_length': "تعداد کاراکترها بیش از حد مجاز هست",
                'required': 'این فیلد نباید خالی باشد',
                'unique': "کاربری با این شماره موبایل از قبل وجود دارد",
            },
            'sender_mail': {
                'max_length': "تعداد کاراکترها بیش از حد مجاز هست",
                'required': 'این فیلد نباید خالی باشد',
                'password_too_short': 'باید حداقل %(min_length)d کاراکتر داشته باشد',
                'password_too_similar': 'رمز عبور شما خیلی شبیه به %(verbose_name)s میباشد',
                'password_too_common': 'رمز عبور شما خیلی ساده انتخاب شده است',
                'password_entirely_numeric': 'بجز اعداد باید شامل حروف و کاراکترهای دیگر هم باشد',
            },
            'sender_phone': {
                'max_length': "تعداد کاراکترها بیش از حد مجاز هست",
                'required': 'این فیلد نباید خالی باشد',
                'unique': "کاربری با این شماره موبایل از قبل وجود دارد",
            },
        }
        help_texts = {

        }
        field_classes={

        }





class ProjectForm(TranslatableModelFormMixin, forms.ModelForm, metaclass=TranslatableModelFormMetaclass):
    # images_list = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), help_text='<br>maximum is 5 images')      # solution 2

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        initial = None
        if 'instance' in kwargs:
            if kwargs['instance'] is not None:
                initial = [img.image for img in kwargs['instance'].images.all()]
        self.fields['images_list'] = forms.FileField(required=False, widget=MyFileInput(imgs=initial, attrs={'multiple': True}), help_text='<br>maximum is 5 images')
            # Note :
            # HTML file input fields are never populated with existing data - this is a browser restriction, nothing to do with Django.
            # It's a security measure, to stop malicious sites tricking you into uploading arbitrary content from your computer.

    class Meta:
        fields = '__all__'


class ArticleForm(ProjectForm):

    class Meta(ProjectForm.Meta):
        model = Article


class LibraryForm(ProjectForm):

    class Meta(ProjectForm.Meta):
        model = Library


class ApplicationForm(ProjectForm):

    class Meta(ProjectForm.Meta):
        model = Application
