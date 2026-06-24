from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'amount', 'method', 'status', 'paid_at', 'created_at')
    list_filter = ('method', 'status')
    search_fields = ('order__id',)
    ordering = ('-created_at',)