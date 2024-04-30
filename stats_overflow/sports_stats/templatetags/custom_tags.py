from django import template

register = template.Library()

@register.filter
def get_field(value, arg):
    return getattr(value, arg, '')
