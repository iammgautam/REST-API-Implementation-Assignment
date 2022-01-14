from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import User
from .serializers import WriteUserSerializer, ReadUserSerializer

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ("first_name", "last_name")
    ordering_fields = ("age",)

    def get_serializer_class(self):
        if self.action in ("list", 'retrieve'):
            return ReadUserSerializer
        return WriteUserSerializer