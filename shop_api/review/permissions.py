from rest_framework.permissions import BasePermission

class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.author == request.user