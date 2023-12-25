from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Просматривать список могут  только авторизованные пользователи
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Разрешения на чтение разрешены для любого запроса, поэтому мы всегда будем
        # разрешать запросы GET, HEAD, or OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешения на запись есть только у автора сообщения
        return obj.author == request.user