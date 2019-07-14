from django.contrib import admin
from .models import MenuItem, Topping, OrderItem, Order, Extra

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(MenuItem)
admin.site.register(Topping)
admin.site.register(Extra)
