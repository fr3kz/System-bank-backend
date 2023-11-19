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

from accounts.models import Account
from .serializers import UserSerializer, LoginSerializer, RegisterSerializer
from .models import User


# Create your views here.

class UserList(APIView):

    def get(self, request):
        users = User.objects.all()
        usr_serializer = UserSerializer(users, many=True)
        return Response(usr_serializer.data)


class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data,
                                     context={'request': self.request})
        bool = serializer.is_valid(raise_exception=False)
        if bool:
            user = serializer.validated_data['user']

            login(request, user)

            sessionid = request.session.session_key
            csrf_token = get_token(request)

            contex = {'sessionid': sessionid, 'csrf': csrf_token, 'userid': user.id, 'username': user.username,'value':''}
            return Response(contex, status=status.HTTP_202_ACCEPTED)
        contex = {'value':'error','error':serializer.errors}
        return Response(contex, status=status.HTTP_400_BAD_REQUEST)

class RegisterUser(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        register_serializer = RegisterSerializer(data=self.request.data,
                                     context={'request': self.request})

        if register_serializer.is_valid(raise_exception=True):
            user = register_serializer.validated_data['usr']

            login(request, user)



            import random

            temporary_number = random.randint(100000,999999)
            while Account.objects.filter(account_number=temporary_number).exists():
                temporary_number = random.randint(100000,999999),
            account = Account.objects.create(account_owner=user, account_type=1, account_number=int(temporary_number),account_balance=0,is_Main=True)


            sessionid = request.session.session_key
            csrf_token = get_token(request)
            contex = {'sessionid': sessionid, 'csrf': csrf_token, 'userid': user.id, 'username': user.username}
            return Response(contex, status=status.HTTP_202_ACCEPTED)


class UserDetail(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)


class CSRFView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        csrf_token = get_token(request)
        return JsonResponse({'csrf': csrf_token})