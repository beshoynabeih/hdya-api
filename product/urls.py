from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='products')
router.register(r'product_imgs', views.ProductPictureViewSet, basename='product_images')
router.register(r'occassions', views.OccassionViewSet, basename='occassions')
router.register(r'RelationShips', views.RelationShipViewSet, basename='relationships')
router.register(r'categories', views.CategoryViewSet, basename='categories')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
