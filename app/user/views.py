"""
views for user API
"""

from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import (
    UserSerializer,
    AuthToeknSerializer,
)


class CreateUserView(generics.CreateAPIView):
    """create new user api in sysytem"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """ Create new auth token for user"""
    serializer_class = AuthToeknSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrived and return the authenticated user"""
        return self.request.user
