from rest_framework import serializers
from .models import Product,Order,OrderItem,User


# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
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