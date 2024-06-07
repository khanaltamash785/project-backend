from django.shortcuts import render

# Create your views here.

from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response

from rest_framework.decorators import api_view


@api_view(['GET'])
def getProduct(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createProduct(request):
    if request.method == 'POST':
        ProductSerializer(data=request.data)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
