from rest_framework import routers
from django.urls import path, include
from . import views
from HdyaBack import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet, basename='users')
urlpatterns = [
    path('', include(router.urls)),
    path('password/reset/', views.password_reset_page),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
