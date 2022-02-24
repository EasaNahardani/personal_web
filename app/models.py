from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.utils.safestring import mark_safe
from parler.models import TranslatableModelMixin
from parler.managers import TranslatableManager
from .fields import AllTranslatedFields
from .validators import PhoneNumberValidator



def get_image_filename(instance, filename):
    name = instance.project.title
    return "project_images/%s/%s" % (name, filename)



class Image(models.Model):
    # project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)    raise error because project is abstract
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE,
                                    # related_name='images',            # this is not work
                                     limit_choices_to={'model__in':(
                                     'Article',
                                     'Application',
                                     'Library')})
    object_id = models.PositiveIntegerField()
    project = GenericForeignKey('content_type', 'object_id')
    image = models.ImageField(upload_to=get_image_filename, verbose_name='Image')


    def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" style="height:100px;border-radius:8px;" />' % self.image.url)
        else:
            return 'No Image'

    image_tag.short_description = 'Image'





class Project(TranslatableModelMixin, models.Model):# if this inherit TranslatableModel, so you dont need TranslatableManager()
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    #CATEGORY_CHOICES = (
    #    ('article', 'Article'),
    #    ('mobile', 'Mobile'),
    #    ('library', 'Library'),
    #)
    url = models.URLField(blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    images = GenericRelation(Image, blank=True, null=True)   #  naming images raise an error :
                                      # TypeError: Direct assignment to the reverse side of a related set is prohibited. Use +.set() instead.
                                      # because i had a field in my form named images

    objects = TranslatableManager()

    class Meta:
        abstract = True
        ordering = ('-created',)

    def __str__(self):
        return self.title




class Article(Project):
    translations = AllTranslatedFields(
        title=models.CharField(max_length=250),
        description = models.TextField(),
    )


class Application(Project):
    translations = AllTranslatedFields(
        title=models.CharField(max_length=250),
        language = models.CharField(max_length=250),
    )
    technologies = models.TextField(),


class Library(Project):
    translations = AllTranslatedFields(
        title=models.CharField(max_length=250),
        language = models.CharField(max_length=250),
    )
    technologies = models.TextField(),

    class Meta:
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'




class Skill(models.Model):
    name = models.CharField(max_length=200)
    level = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name





class ContactMessage(models.Model):
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=255)
    sender_mail = models.EmailField(_('Email Address'),
                            error_messages={
                                'unique': _("A user with that email already exists."),
                            },
                            blank=True,)
    phone_validator = PhoneNumberValidator()
    sender_phone = models.CharField(_('Phone Number'), validators=[phone_validator], max_length=16,
                            blank=True,)

    class Meta:
        ordering = ('-sent_at',)


    def __str__(self):
        return f'sent at {self.sent_at}'

   # if you want to show errors to user, so you should write this code in clean() nor save()
    def clean(self):
        if not (self.sender_mail or self.sender_phone):
            # raise ValidationError("Both email and phone number can not be blank")              # this is showed in above and global
            raise ValidationError({
                'sender_phone': ValidationError(_('Both this field and phone number can not be blank.please fill one of them'), code='required_together_phone'),
                'sender_mail': ValidationError(_('Both this field and email can not be blank.please fill one of them.'), code='required_together_phone'),
            })
        super().clean()
