import json
from .models import *


def cartData(request):
	
	customer = request.user.customer
	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	items = order.orderitem_set.all()
	cartItems = order.get_cart_items
	price = order.get_cart_total

	return {'cartItems':cartItems ,'order':order, 'items':items , 'price':price}

