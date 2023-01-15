from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MessageView

router_messages = DefaultRouter()

router_messages.register('messages', MessageView, basename='messages')

urlpatterns = [
    path('', include(router_messages.urls))
]