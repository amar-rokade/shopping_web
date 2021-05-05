from django.contrib import admin
from .models import User,Seller,Buyer,ItemModel,cart,Buy
# Register your models here.
admin.site.register(User)
admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(ItemModel)
admin.site.register(cart)
admin.site.register(Buy)