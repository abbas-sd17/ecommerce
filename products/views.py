from django.http import HttpResponse

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from products.models import Products
from rest_framework import status


# Create your views here.
def hello(request):
    data= Products.objects.all()
    d=data[0]
    print(data[0].name)
    d.name="Apple"
    d.save()
    data=Products.objects.all()
    print( d.name)

    return HttpResponse("hello world")

@api_view(['GET'])
def getproducts(request):
    data=Products.objects.all()
    serializer = ProductSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product_by_id(request, product_id):
    try:
        product = Products.objects.get(id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
