from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import * #ProductSerializer, OccassionSerializer , ProductPictureSerializer
from .models import *


# Create your views here.

# class Products(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductPictureViewSet(viewsets.ModelViewSet):
    queryset = ProductPicture.objects.all()
    serializer_class = ProductPictureSerializer


class OccassionViewSet(viewsets.ModelViewSet):
    queryset = Occassion.objects.all()
    serializer_class = OccassionSerializer

class RelationShipViewSet(viewsets.ModelViewSet):
    queryset = RelationShip.objects.all()
    serializer_class = RelationShipSerializer

