from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Function Based View
@api_view(['GET','POST','DELETE'])
def product_list(request):
    prodcust = Product.objects.all()
    serializer = ProductSerializer(prodcust,many = True)
    return Response(serializer.data)



@api_view(['GET'])
def product_detail(request,pk):
    product = get_object_or_404(Product,id=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)