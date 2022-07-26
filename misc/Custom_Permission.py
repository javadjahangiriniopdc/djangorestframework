from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # put pacth delete
        return obj.user == request.user

    def has_permission(self, request, view):
        # read create
        return request.user and request.user.is_authenticated
