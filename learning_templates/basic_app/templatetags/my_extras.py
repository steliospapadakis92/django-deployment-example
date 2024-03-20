#to put all my extra templates in this file

from django import template
register = template.Library()

@register.filter
def cutout(value, arg): #takes value and argument; this cuts out all values of arg from the string. We replace arg with ''
    return value.replace(arg, '')
