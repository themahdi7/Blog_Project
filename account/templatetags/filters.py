from django import template


register = template.Library()


@register.filter
def counter(value):
    return value.count()
    # return number of objects
