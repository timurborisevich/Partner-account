from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        # Если get или head запрос сразу даем доступ
        if request.method in permissions.SAFE_METHODS:
            return True
        # Иначе проверям, что пользователь авторизован и он админ
        return bool(request.user and request.user.is_staff)