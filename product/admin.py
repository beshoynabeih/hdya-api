from django.contrib import admin
from product.models import *


class ProductPictureinline(admin.TabularInline):
    model = ProductPicture


class ProductPictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image')
    list_filter = ('product',)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'name', 'age_from', 'age_to', 'category', 'user', 'price', 'gender', 'occassions_list', 'relationships_list')
    inlines = [ProductPictureinline]

    def occassions_list(self, obj):
        return ", ".join([f"{a.id}|{a.name}" for a in obj.occassions.all()])

    def relationships_list(self, obj):
        return ", ".join([f"{a.id}|{a.name}" for a in obj.relationships.all()])


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'rate', 'user', 'body')
    list_display_links = ('id', 'product')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'quantity', 'product', 'status', 'created_at', 'updated_at')


admin.site.register(ProductPicture, ProductPictureAdmin)
admin.site.register(RelationShip)
admin.site.register(Occassion)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Order, OrderAdmin)
