from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserView

router_users = DefaultRouter()

router_users.register('users', UserView, basename='users')

urlpatterns = [
    path('', include(router_users.urls)),
]