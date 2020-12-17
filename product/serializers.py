from .models import *  # Product , Category , Occassion , RelationShip
from rest_framework import serializers
from django.utils import timezone


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ('url', 'id', 'title', 'description')
        extra_kwargs = {
            'url': {'view_name': 'categories-detail'}
        }


class OccassionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Occassion
        fields = ('url', 'id', 'name', 'description')
        extra_kwargs = {
            'url': {'view_name': 'occassions-detail'}
        }


class RelationShipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RelationShip
        fields = ('url', 'id', 'name', 'description')
        extra_kwargs = {
            'url': {'view_name': 'relationships-detail'}
        }


class ProductPictureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductPicture
        fields = ('url', 'id', 'img_url')
        extra_kwargs = {
            'url': {'view_name': 'product_images-detail'}
        }


class ProductSerializer(serializers.ModelSerializer):
    # user_name = serializers.CharField(source="user_id.user.username", read_only=True)
    category = serializers.HyperlinkedIdentityField(view_name='categories-detail')
    occassions = serializers.HyperlinkedIdentityField(many=True, view_name='occassions-detail')
    relationships = serializers.HyperlinkedIdentityField(many=True, view_name='relationships-detail')
    # user = serializers.CharField(
    #     default=serializers.CurrentUserDefault()
    # )

    class Meta:
        model = Product
        fields = ('id',
                  'user',
                  'category',
                  'occassions',
                  'relationships',
                  'name',
                  'details',
                  'price',
                  'age_from',
                  'age_to',
                  'gender',
                  'is_featured',
                  'created_at')
        read_only_fields = ('is_featured', 'user')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'


class ProductReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReport
        fields = '__all__'


class ReviewReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewReport
        fields = '__all__'

