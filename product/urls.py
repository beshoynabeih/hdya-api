from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='products')
router.register(r'product_imgs', views.ProductPictureViewSet, basename='product_images')
router.register(r'occassions', views.OccassionViewSet, basename='occassions')
router.register(r'RelationShips', views.RelationShipViewSet, basename='relationships')
router.register(r'categories', views.CategoryViewSet, basename='categories')
router.register(r'reviews', views.ReviewViewSet, basename='reviews')
router.register(r'productreports', views.ProductReportViewSet, basename='productreports')
router.register(r'reviewreport', views.ReviewReportViewSet, basename='reviewreport')
# router.register(r'test', views.TestViewSet, basename='test')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('product_image/<int:pk>/', views.ProductImageDetail.as_view(), name='product_image-detail'),
    path('product_image/', views.ProductImageCreate.as_view(), name='product_image-create'),
    path('my/products/', views.UserProducts.as_view(), name='user_products'),
    path('product/reviews/', views.ProductReview.as_view(), name='product_reviews'),
    path('product/search/', views.ProductSearch.as_view(), name='product_search'),
    path('orders/', views.OrderList.as_view(), name='orders'),
    path('my/orders/', views.MyOrderList.as_view(), name='my_orders'),
    path('orders/<int:pk>/', views.OrderCancel.as_view(), name='orders'),
]
