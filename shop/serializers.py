from rest_framework import serializers
from .models import Product, CartItem, Cart, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source = 'category.name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description', 'category', 'category_name', 'price', 'stock', 'image', 'is_active', 'created_at', 'updated_at']

class CartItemSerializer(serializers.ModelSerializer):
   product_name = serializers.CharField(source = 'product.name', read_only=True) 
   product_price = serializers.DecimalField(source = 'product.price', max_digits=10, decimal_places=2, read_only=True) 

   class Meta:
       model = CartItem
       fields = ['id', 'cart', 'product', 'product_name', 'product_price', 'quantity', 'added_at']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'items']