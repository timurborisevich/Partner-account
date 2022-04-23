from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/v1/users', CustomUserViewSet, basename='users')
router.register(r'api/v1/user', ProfileCustomUserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/user_logout/', LogoutView.as_view(), name = 'user_logout')
]
