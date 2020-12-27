from django.contrib import admin
from product.models import *


class ProductPictureinline(admin.TabularInline):
    model = ProductPicture


class ProductPictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image')
    list_filter = ('product',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'price', 'gender')
    inlines = [ProductPictureinline]


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'product_id', 'user', 'body')
    list_display_links = ('id', 'product', 'product_id')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'quantity', 'product', 'status', 'created_at', 'updated_at')


admin.site.register(ProductPicture, ProductPictureAdmin)
admin.site.register(RelationShip)
admin.site.register(Occassion)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Order, OrderAdmin)

