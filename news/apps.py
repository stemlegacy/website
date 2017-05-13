from django.apps import AppConfig
from django import template
register = template.Library()

class NewsConfig(AppConfig):
    name = 'news'
@register.filter
def return_item(l, i):
        try:
            return l[i]
        except:
            return None