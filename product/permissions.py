from rest_framework import permissions


class ProductOwner(permissions.BasePermission):
    message = "unauthorized user"

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS that do not write data like GET, OPTION, HEAD
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user


class ProductImageOwner(permissions.BasePermission):
    message = "unauthorized user"

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS that do not write data like GET, OPTION, HEAD
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.product.user


class SubmitReview(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.id or False


class OrderOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user