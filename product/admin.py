from django.contrib import admin
from product.models import *


class ProductPictureinline(admin.TabularInline):
    model = ProductPicture


class ProductPictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image')
    list_filter = ('product',)


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductPictureinline]


admin.site.register(ProductPicture, ProductPictureAdmin)
admin.site.register(RelationShip)
admin.site.register(Occassion)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Test)
