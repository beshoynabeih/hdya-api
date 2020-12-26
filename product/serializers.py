from .models import *  # Product , Category , Occassion , RelationShip
from rest_framework import serializers, status, validators
from rest_framework.response import Response
from django.utils import timezone


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'description')


class OccassionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occassion
        fields = ('id', 'name', 'description')


class RelationShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationShip
        fields = ('id', 'name', 'description')


class ProductPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPicture
        fields = ('id', 'image', 'product')


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    occassions = serializers.PrimaryKeyRelatedField(many=True, queryset=Occassion.objects.all(), required=False)
    relationships = serializers.PrimaryKeyRelatedField(many=True, queryset=RelationShip.objects.all(), required=False)
    images = ProductPictureSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ('id',
                  'name',
                  'details',
                  'category',
                  'price',
                  'age_from',
                  'age_to',
                  'gender',
                  'is_featured',
                  'user',
                  'occassions',
                  'relationships',
                  'images',
                  'created_at',
                  'updated_at',
                  )
        read_only_fields = ('is_featured', 'created_at', 'updated_at', 'user')

    def validate(self, attrs):
        if attrs['age_from'] > attrs['age_to']:
            raise serializers.ValidationError('invalid valud for age to')
        attrs['user'] = self.context['request'].user
        return attrs

    def create(self, validated_data):
        print(validated_data)
        product = super(ProductSerializer, self).create(validated_data)
        # ProductPicture.objects.create(product=product, image=image)
        return product


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReport
        fields = '__all__'


class ReviewReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewReport
        fields = '__all__'
