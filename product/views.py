from django.shortcuts import render
from rest_framework import viewsets, views, status
from .serializers import *  # ProductSerializer, OccassionSerializer , ProductPictureSerializer
from .models import *
from .permissions import ProductOwner, ProductImageOwner
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
import os
# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    __basic_fields = ('name',
                      'price',
                      'gender',
                      'age_from',
                      'age_to',
                      'category',
                      'user',
                      'occassions',
                      'is_featured')

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields
    permission_classes = [ProductOwner]


    # def recentFiveProducts(queryset):
    # lastest_five = Product.objects.order_by('-created_at')[:5]


class ProductPictureViewSet(viewsets.ModelViewSet):
    queryset = ProductPicture.objects.all()
    serializer_class = ProductPictureSerializer


# class TestViewSet(viewsets.ModelViewSet):
#     queryset = Test.objects.all()
#     serializer_class = TestSerializer


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


class ProductImageDetail(views.APIView):

    permission_classes = [ProductImageOwner, ]

    def get_object(self, pk):
        try:
            return ProductPicture.objects.get(pk=pk)
        except ProductPicture.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        image = self.get_object(pk)
        serializer = ProductPictureSerializer(image)
        return Response(serializer.data)

    def delete(self, request, pk):
        image = self.get_object(pk)
        self.check_object_permissions(request, image)
        path = image.image.path
        if os.path.isfile(path):
            os.remove(path)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

class ProductReportViewSet(viewsets.ModelViewSet):
    queryset = ProductReport.objects.all()
    serializer_class = ProductReportSerializer

class ReviewReportViewSet(viewsets.ModelViewSet):
    queryset = ReviewReport.objects.all()
    serializer_class = ReviewReportSerializer