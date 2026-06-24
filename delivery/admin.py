from django.contrib import admin
from .models import Delivery


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('order', 'delivery_type', 'status', 'pickup_date', 'delivered_at')
    list_filter = ('delivery_type', 'status')
    search_fields = ('order__id',)
    ordering = ('-created_at',)