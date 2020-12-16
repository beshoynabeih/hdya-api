from .models import *  # Product , Category , Occassion , RelationShip
from rest_framework import serializers
from django.utils import timezone


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OccassionSerializer(serializers.ModelSerializer):
    # product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Occassion
        fields = '__all__'
    

class RelationShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationShip
        fields = '__all__'



class ProductPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPicture
        fields = '__all__'
        # read_only_fields = ('product',)
        

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category_id.title", read_only=True)
    user_name = serializers.CharField(source="user_id.user.username", read_only=True)
    # occassions_name = serializers.CharField(source ='occassions')

    occassions = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Occassion.objects.all()
    )
    relationships = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=RelationShip.objects.all(),
    )

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('is_featured',)





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
