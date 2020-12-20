from .models import *  # Product , Category , Occassion , RelationShip
from rest_framework import serializers
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


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # user_name = serializers.CharField(source="user_id.user.username", read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    occassions = serializers.PrimaryKeyRelatedField(many=True, queryset=Occassion.objects.all())
    relationships = serializers.PrimaryKeyRelatedField(many=True, queryset=RelationShip.objects.all())
    productpicture_set = ProductPictureSerializer(many=True, required=False)
    user = serializers.CharField(
        default=serializers.CurrentUserDefault()
    )
    # test_set = TestSerializer(many=True)

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
                  'created_at',
                  'productpicture_set',)
        read_only_fields = ('is_featured', 'user')

    def create(self, validated_data):
        print(validated_data)
        tests = validated_data.pop('productpicture_set')
        product = super(ProductSerializer, self).create(validated_data)
        for test in tests:
            print(type(test))
            # Test.objects.create(product=product, **test)
            ProductPicture.objects.create(product=product, image='')
        return product


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
