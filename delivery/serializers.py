from rest_framework import serializers
from .models import Delivery


class DeliverySerializer(serializers.ModelSerializer):

    order_id = serializers.CharField(source='order.id', read_only=True)

    class Meta:
        model = Delivery
        fields = [
            'id',
            'order',
            'order_id',
            'delivery_type',
            'delivery_address',
            'status',
            'pickup_date',
            'delivered_at',
            'created_at'
        ]