import re
from django import template
from django.utils import translation
from django.urls import translate_url


register = template.Library()


def get_digit(matchobj):
    digit = matchobj.group(0) # The entire match - it is a string
    d = int(digit)
    return '۰۱۲۳۴۵۶۷۸۹'[d]


@register.filter(name='e2p')
def get_farsi_numbers(text):
    if isinstance(text, int):
        text = str(text)
    elif not isinstance(text, str):
        return text
    return re.sub(r'\d', get_digit, text) # advanced version of replace()


@register.filter(name='splitter')
def get_technologies(s):
    return re.split('\s+', s)



@register.filter(name='addClass')
def add_class(bf, css_class):
    if not isinstance(css_class, str):
        css_class = str(css_class)
    attrs = bf.field.widget.attrs
    if 'class' in attrs:
        attrs['class'] += ' ' + css_class
    else:
        attrs['class'] = css_class
    return bf



@register.filter(name='translated_url')
def get_translated_url(url, lang_code):
    #cur_language = translation.get_language()
    #try:
    #    translation.activate('fa')
    #    text = translation.gettext('Projects')
    #finally:
    #    translation.activate(cur_language)
    # روش بالا فقط از انلیسی به زبانهای دیگر کار کرد و برعکس کار نمیکند
    return translate_url(url, lang_code)
