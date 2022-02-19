import re
from django import template


register = template.Library()


@register.filter(name='splitter')
def get_technologies(s):
    print(re.split('\s+', s))
    print('#############')
    return re.split('\s+', s)
