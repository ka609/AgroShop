from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description'
        ]


class ProductSerializer(serializers.ModelSerializer):

    producer_name = serializers.CharField(
        source='producer.username',
        read_only=True
    )

    class Meta:
        model = Product
        fields = [
            'id',
            'producer',
            'producer_name',
            'category',
            'name',
            'description',
            'price',
            'stock',
            'image',
            'is_available',
            'created_at',
            'updated_at'
        ]