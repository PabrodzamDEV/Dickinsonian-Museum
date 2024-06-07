from django import template

register = template.Library()


def chunk(value, arg):
    return [value[i:i + arg] for i in range(0, len(value), arg)]


register.filter('chunk', chunk)
