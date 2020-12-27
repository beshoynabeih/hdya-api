from django.db import models
from django.utils import timezone
from authentication.models import User


class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title


class Occassion(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class RelationShip(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=45)
    details = models.TextField(max_length=3000)
    price = models.FloatField()
    age_from = models.PositiveIntegerField()
    age_to = models.PositiveIntegerField()
    gender = models.CharField(
        null=True,
        max_length=50,
        choices=[
            ('m', 'Male'),
            ('f', 'female'),
            ('b', 'both')
        ])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    occassions = models.ManyToManyField(Occassion)
    relationships = models.ManyToManyField(RelationShip)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pimage = models.ImageField(upload_to='static/products/images/')

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.name


class ProductPicture(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='static/products/images/', verbose_name='Image')

    def __str__(self):
        return self.product.name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=1000)
    rate = models.CharField(
        null=True,
        max_length=50,
        choices=[
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
        ])
    created_at = models.DateTimeField(auto_now_add=True)


class ProductReport(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


class ReviewReport(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=2, choices=[
        ('p', 'in processing'),
        ('s', 'shipped'),
        ('e', 'delivered'),
        ('r', 'returned'),
        ('c', 'cancelled'),
    ], default='p')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
