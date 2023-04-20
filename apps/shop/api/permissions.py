from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Allows access only to admin users for unsafe methods (POST, PUT, PATCH, DELETE).
    All users have access to safe methods (GET, HEAD, OPTIONS).

    To use this permission class, simply add it to the 'permission_classes' attribute
    of your view or viewset.

    For example:
        class MyViewSet(viewsets.ModelViewSet):
            queryset = MyModel.objects.all()
            serializer_class = MyModelSerializer
            permission_classes = [IsAdminOrReadOnly]
    """

    def has_permission(self, request: Request, view: ViewSet) -> bool:
        """
        Returns True if the request method is safe (GET, HEAD, OPTIONS) or if the
        requesting user is an admin. Returns False otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Allows access only to the object owner for unsafe methods (POST, PUT, PATCH, DELETE).
    All users have access to safe methods (GET, HEAD, OPTIONS).

    To use this permission class, simply add it to the 'permission_classes' attribute
    of your view or viewset.

    For example:
        class MyViewSet(viewsets.ModelViewSet):
            queryset = MyModel.objects.all()
            serializer_class = MyModelSerializer
            permission_classes = [IsOwnerOrReadOnly]

    """

    def has_object_permission(self, request: Request, view: ViewSet, obj: object) -> bool:
        """
        Returns True if the request method is safe (GET, HEAD, OPTIONS) or if the
        requesting user is the owner of the object. Returns False otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
