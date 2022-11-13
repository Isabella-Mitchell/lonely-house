from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, no_nights):
    """Allows the subtotal of cart can be seen anywhere on the site"""
    return price * no_nights
