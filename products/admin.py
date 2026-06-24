from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'producer', 'category', 'price', 'stock', 'is_available')
    list_filter = ('is_available', 'category')
    search_fields = ('name', 'producer__username')
    ordering = ('-created_at',)