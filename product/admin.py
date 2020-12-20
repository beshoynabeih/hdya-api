from django.contrib import admin
from product.models import Product, Category, RelationShip, Occassion, ProductPicture


class ProductPictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'img_url')
    list_filter = ('product',)


admin.site.register(ProductPicture, ProductPictureAdmin)
admin.site.register(RelationShip)
admin.site.register(Occassion)
admin.site.register(Category)
admin.site.register(Product)
