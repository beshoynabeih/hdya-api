from django.shortcuts import render
from rest_framework import viewsets
from .serializers import * #ProductSerializer, OccassionSerializer , ProductPictureSerializer
from .models import *
from .permissions import ProductOwner
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


        


class ProductViewSet(viewsets.ModelViewSet):
    __basic_fields = ('name', 'price', 'gender','age_from'  ,'age_to' ,'category' , 'user' , 'occassions' , 'is_featured', 'relationships' )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields



class ProductPictureViewSet(viewsets.ModelViewSet):
    queryset = ProductPicture.objects.all()
    serializer_class = ProductPictureSerializer


class OccassionViewSet(viewsets.ModelViewSet):
    queryset = Occassion.objects.all()
    serializer_class = OccassionSerializer

class RelationShipViewSet(viewsets.ModelViewSet):
    queryset = RelationShip.objects.all()
    serializer_class = RelationShipSerializer

    permission_classes = [ProductOwner]


# class OccassionViewSet(viewsets.ModelViewSet):
#     queryset = Occassion.objects.all()
#     serializer_class = OccassionSerializer
