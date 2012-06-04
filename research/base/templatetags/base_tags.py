
import re
from mezzanine import template
from django.core.urlresolvers import RegexURLResolver
from research import urls


register = template.Library()

@register.simple_tag
def active(request, pattern=''):

    path = request.path

    if pattern == '/' and pattern != path:
        return ''


    if re.search(pattern, path):
        return 'active'

    else:
        return ''
