from rest_framework.permissions import BasePermission

class PostPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method in ['POST', 'PUT', 'DELETE']:
            return request.user.is_authenticated

class PostDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'POST', 'DELETE']:
            return request.user.is_authenticated
            