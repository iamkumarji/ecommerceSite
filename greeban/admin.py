from django.contrib import admin
from .models import Product, UserData, OTP, OrderDetails, Order, Promotions

# Register your models here.

admin.site.register(Product)
admin.site.register(UserData)
admin.site.register(OTP)
admin.site.register(OrderDetails)
admin.site.register(Order)
admin.site.register(Promotions)

