from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


class IsStaffOrReadonly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )



class IsAuthorOrReadonly(BasePermission):
    def has_object_permission(self, request, view, obj):
        
        if request.method in SAFE_METHODS:
            return True

        
        return bool(request.user.is_authenticated and obj.author == request.user or
                    request.user.is_superuser)



class SuperUserOrReadonly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS and request.user.is_authenticated or
            request.user.is_authenticated and request.user.is_superuser
        )


