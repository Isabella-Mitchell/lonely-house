from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, no_nights):
    return price * no_nights
