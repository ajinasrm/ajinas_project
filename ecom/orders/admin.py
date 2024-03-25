from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('pant_id', 'customer_name', 'customer_email', 'color', 'size', 'material', 'price', 'quantity')
    search_fields = ('pant_id', 'customer_name', 'customer_email', 'color', 'size', 'material')
    list_filter = ('color', 'size', 'material')

admin.site.register(Order, OrderAdmin)
