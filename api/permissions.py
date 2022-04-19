from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS


class IsStaffOrReadonly(BasePermission):
    # only staff users can add articles
    # unstaff users -> readonly
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )



class IsAuthorOrReadonly(BasePermission):
    # staff users can only access their own articles to update or delete them
    def has_object_permission(self, request, view, obj):
        
        if request.method in SAFE_METHODS:
            return True

        
        return bool(request.user.is_authenticated and obj.author == request.user or
                    request.user.is_superuser)



class SuperUserOrReadonly(BasePermission):
    # only superuser can create, update or delete users
    # staff -> readonly
    # auth user, anonym users can not see anything
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS and 
            request.user.is_authenticated and request.user.is_staff or
            request.user.is_authenticated and request.user.is_superuser
        )


