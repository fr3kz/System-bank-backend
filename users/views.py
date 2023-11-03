from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer,LoginSerializer
from .models import User

# Create your views here.

class UserList(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self,request):
        users = User.objects.all()
        usr_serializer = UserSerializer(users,many=True)
        return Response(usr_serializer.data)
class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data,
                                                 context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        login(request, user)

        sessionid = request.session.session_key
        csrf_token = get_token(request)

        contex={'sessionid':sessionid,'csrf':csrf_token,'userid':user.id,'username':user.username}
        return Response(contex, status=status.HTTP_202_ACCEPTED)

class UserDetail(APIView):
    def get(self,request,id):
        user = get_object_or_404(User,id=id)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)


