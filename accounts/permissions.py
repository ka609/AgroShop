from rest_framework.permissions import BasePermission


class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'client'


class IsProducteur(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'producteur'


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.producer == request.user