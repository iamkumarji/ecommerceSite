# to create mapping between prod and quantity so to display the quantity
from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    #cart.pop('null')
    keys = cart.keys()
    # print(cart)
    for id in keys:
        # print(type(id), type(product.id))
        # print(id, product.id)
        if id != '':
            if id != "null" and int(id) == product.id:
                return True
    return False


@register.filter(name='cart_prod_quantity')
def cart_prod_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if id != '':
            if id != "null" and int(id) == product.id:
                return cart.get(id)
    return 0


@register.filter(name='price_total')
def price_total(product, cart):
    return product.product_price * cart_prod_quantity(product, cart)


@register.filter(name='total_cart_price')
def total_cart_price(products, cart):
    sum = 0
    for p in products:
        sum += price_total(p, cart)
    return sum


@register.filter(name='shipping_fees')
def shipping_fees(products, cart):
    return 39


@register.filter(name='final_cart_amount_incl_shipping')
def final_cart_amount_incl_shipping(products, cart):
    return shipping_fees(products, cart) + total_cart_price(products, cart)

