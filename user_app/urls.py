from collections import UserList
from django.urls import path
from rest_framework import routers
from user_app.views import UserModelViewSet

router = routers.SimpleRouter()
router.register(r'users', UserModelViewSet, basename='users')

urlpatterns = [
] + router.urls
