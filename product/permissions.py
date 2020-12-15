from rest_framework import permissions


class ProductOwner(permissions.BasePermission):
    message = "unauthorized user"

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS that do not write data like GET, OPTION, HEAD
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user
