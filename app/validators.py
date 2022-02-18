from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _



@deconstructible
class PhoneNumberValidator(validators.RegexValidator):
    regex = r'^\+?\d{10,15}$'
    message = """ شماره موبایل مانند
        6**0912198915
        وارد شود"""
    flags = 0 # if flags is not 0, so regex must be str( default flags is 0 )
