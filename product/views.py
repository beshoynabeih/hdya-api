from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import ProductSerializer, OccassionSerializer
from .models import *
from .permissions import ProductOwner

# Create your views here.

# class Products(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = [ProductOwner]
# class OccassionViewSet(viewsets.ModelViewSet):
#     queryset = Occassion.objects.all()
#     serializer_class = OccassionSerializer
