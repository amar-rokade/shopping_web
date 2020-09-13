from django import template
register = template.Library()
from accounts.models import cart

@register.simple_tag
def is_cart(item_num,user):
    is_cart_n = cart.objects.filter(user=user,item=item_num)
    return is_cart_n


    

