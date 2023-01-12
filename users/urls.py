from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserView

router_v1 = DefaultRouter()

router_v1.register('users', UserView, basename='users')

urlpatterns = [
    path('', include(router_v1.urls)),
]