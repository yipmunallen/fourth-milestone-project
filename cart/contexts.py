from decimal import Decimal
from django.conf import settings


def cart_contents(request):

    cart_items = []
    subtotal = 0
    product_count = 0

    if subtotal < settings.FREE_DELIVERY_THRESHOLD:
        delivery = subtotal * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - subtotal
    else:
        delivery = 0
        free_delivery_delta = 0
    
    total = delivery + subtotal
    
    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'total': total,
    }

    return context