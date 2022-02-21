import re
from django import template


register = template.Library()


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
