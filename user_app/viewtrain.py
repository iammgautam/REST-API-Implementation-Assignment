from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from .serializers import UserSerializers
from .models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    
def userlist(request):
    users = User.objects.all()
    return render(request, 'user_app/user_list.html', {'users':users})

class UserDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'add_user.html'

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializers(user)
        return Response({'serializer': serializer, 'user': user})

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializers(user, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'user': user})
        serializer.save()
        return redirect('/user-list/')