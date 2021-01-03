from django.shortcuts import render
from rest_framework import viewsets, views, status
from .serializers import *  # ProductSerializer, OccassionSerializer , ProductPictureSerializer
from .models import *
from .permissions import ProductOwner, ProductImageOwner, SubmitReview, OrderOwner
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.pagination import LimitOffsetPagination
from django.db.models import Q
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


class UserProducts(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        products = Product.objects.filter(user=request.user)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OccassionViewSet(viewsets.ModelViewSet):
    queryset = Occassion.objects.all()
    serializer_class = OccassionSerializer


class RelationShipViewSet(viewsets.ModelViewSet):
    queryset = RelationShip.objects.all()
    serializer_class = RelationShipSerializer

    permission_classes = [ProductOwner]


class ProductImageCreate(views.APIView):
    permission_classes = [ProductOwner]

    def post(self, request):
        if not request.FILES.getlist('image'):
            return Response({"image": "this field is required"}, status=status.HTTP_400_BAD_REQUEST)
        if request.POST.get('product'):
            try:
                product = Product.objects.get(pk=request.POST.get('product'))
            except:
                raise Http404
            self.check_object_permissions(request, product)

            product_images = []
            for image in request.FILES.getlist('image'):
                serializer = ProductPictureSerializer(data={"product": product.id, "image": image})
                if serializer.is_valid():
                    serializer.save()
                    product_images.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(product_images, status=status.HTTP_201_CREATED)
        raise Http404


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


class ProductReportViewSet(viewsets.ModelViewSet):
    queryset = ProductReport.objects.all()
    serializer_class = ProductReportSerializer


class ReviewReportViewSet(viewsets.ModelViewSet):
    queryset = ReviewReport.objects.all()
    serializer_class = ReviewReportSerializer


# class ProductCreate(views.APIView):
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request):
#         if request.method == "POST":
#             self.check_permissions(request)
#             product = ProductSerializer(data=request.data)
#             if product.is_valid():
#                 product.save()
#                 return Response(product.data, status=status.HTTP_201_CREATED)
#             return Response(product.errors)


class ProductReview(views.APIView):
    permission_classes = [SubmitReview]

    def get(self, request):
        reviews = Review.objects.filter(product=request.GET.get('product'))
        return Response(ReviewSerializer(reviews, many=True).data)

    def post(self, request):
        review = ReviewSerializer(data=request.data)
        if review.is_valid():
            review.save(user=request.user)
            return Response(review.data, status=status.HTTP_201_CREATED)
        return Response(review.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderList(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        order = Order.objects.filter(product__user=request.user).exclude(status='c')
        return Response(OrderSerializer(order, many=True).data, status=status.HTTP_200_OK)

    def post(self, request):
        order = OrderSerializer(data=request.data)
        if order.is_valid():
            order.save(user=request.user)
            return Response(order.data, status=status.HTTP_201_CREATED)
        return Response(order.errors, status=status.HTTP_400_BAD_REQUEST)


class MyOrderList(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user).exclude(status='c')
        return Response(OrderSerializer(orders, many=True).data)




class OrderCancel(views.APIView):
    permission_classes = [OrderOwner]

    def delete(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except:
            raise Http404
        self.check_object_permissions(request, order)
        order.status = 'c'
        order.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductSearch(views.APIView, LimitOffsetPagination):

    def relationship_query(self, relationships):
        sub_query = Q(relationships__in=relationships[0])
        for relation in relationships[1:]:
            sub_query |= Q(relationships__in=relation)
        return sub_query

    def occassions_query(self, occassions):
        sub_query = Q(occassions__in=[occassions[0]])
        for occassion in occassions[1:]:
            sub_query |= Q(occasions__in=[occassion])
        return sub_query

    def category_query(self, categories):
        sub_query = Q(category=categories[0])
        for category in categories:
            sub_query |= Q(category=category)
        return sub_query

    def gender_query(self, gender):
        sub_query = Q(gender=gender[0])
        for g in gender:
            sub_query |= Q(gender=g)
        return sub_query

    def get(self, request):
        products = Product.objects.all()
        if 'name' in request.GET:
            products = products.filter(name__icontains=request.GET.get('name'))
        if 'min_price' in request.GET:
            products = products.filter(price__gte=request.GET.get('min_price'))
        if 'max_price' in request.GET:
            products = products.filter(price__lte=request.GET.get('max_price'))
        if 'min_age' in request.GET:
            products = products.filter(age_from__gte=request.GET.get('min_age'))
        if 'max_age' in request.GET:
            products = products.filter(age_to__lte=request.GET.get('max_age'))
        if 'category' in request.GET:
            products = products.filter(self.category_query(request.GET.getlist('category')))
        if 'gender' in request.GET:
            products = products.filter(self.gender_query(request.GET.getlist('gender')))
        if 'relationships' in request.GET:
            products = products.filter(self.relationship_query(request.GET.getlist('relationships')))
        if 'occassions' in request.GET:
            products = products.filter(occassions__in=request.GET.getlist('occassions')).distinct()
        if 'relationships' in request.GET:
            products = products.filter(relationships__in=request.GET.getlist('relationships')).distinct()
        if 'featured' in request.GET:
            products = products.filter(is_featured=request.GET.get('featured'))

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return self.get_paginated_response(serializer.data)