from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from .validators import PhoneNumberValidator



class Skill(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
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

   # if you want to show errors to user, so you should not write this code in save()
    def clean(self):
        if not (self.sender_mail or self.sender_phone):
            # raise ValidationError("Both email and phone number can not be blank")              # this is showed in above and global
            raise ValidationError({
                'sender_phone': ValidationError(_('Both this field and phone number can not be blank.please fill one of them'), code='required_together_phone'),
                'sender_mail': ValidationError(_('Both this field and email can not be blank.please fill one of them.'), code='required_together_phone'),
            })
        super().clean()
