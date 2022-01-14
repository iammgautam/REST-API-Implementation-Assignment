from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import WriteUserSerializer, ReadUserSerializer

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", 'retrieve'):
            return ReadUserSerializer
        return WriteUserSerializer