from django import template

register = template.Library()


@register.filter(name='capitalize')
def capitalize(value):
    """
    capitalize the value, making the first letter capital and lowers the rest
    """
    return value[0].upper() + value[1:].lower()
