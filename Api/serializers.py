from rest_framework import serializers
from .models import Product,Order,OrderItem,User


# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            # 'id',
            'name',
            # 'description',
            'price',
            'stock',
        ]
    
    # Field Level Validation on price field
    def validate_price(self,value):
        if value < 0:
            return serializers.ValidationError(
                'Price Can not be Less Then 0.'
                )
        return value
    
    # Field Level Validation on name field
    def validate_name(self,value):
        if len(value) <= 0:
            raise serializers.ValidationError(
                'Product name can not be empty.'
                )
        return value
    

# OrderItem Serializer
class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = [
            'product',
            'quantity'
        ]


# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many = True,read_only = True)
    total_price = serializers.SerializerMethodField()

    def get_total_price(self,obj):
        order_items = obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)

    class Meta:
        model = Order
        fields = ['order_id','user','created_at','status','items','total_price']