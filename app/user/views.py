"""
views for user API
"""

from rest_framework import generics
from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """create new user api in sysytem"""
    serializer_class = UserSerializer
