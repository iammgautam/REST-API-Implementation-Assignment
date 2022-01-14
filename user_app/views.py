from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import  SearchFilter, OrderingFilter
from rest_framework import status
from rest_framework.response import Response

from .models import User
from .serializers import WriteUserSerializer, ReadUserSerializer

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    filter_backends = (SearchFilter,OrderingFilter,)
    search_fields = ("first_name", "last_name")
    ordering_fields = ("age",)

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_serializer_class(self):
        if self.action in ("list", 'retrieve'):
            return ReadUserSerializer
        return WriteUserSerializer