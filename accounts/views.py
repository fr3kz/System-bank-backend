from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from django.db.models import Q
from rest_framework import status

import datetime
from users.models import User
from .models import Account, Transfer
from .serializers import AccountSerializer, TransferSerializer

class AccountList(APIView):
    #  permission_classes = (permissions.AllowAny,)
    def get(self, request, usrid):
        # do stestowania czy pojdzie user = request.user
        user = User.objects.get(id=usrid)
        Accounts = Account.objects.get(account_owner=user, is_Main=True)
        accout_serializer = AccountSerializer(Accounts, many=False)
        return Response(accout_serializer.data)


class ShowTransferHistory(APIView):
    def get(self, request, accid):
        transfers = Transfer.objects.filter(Q(account1_id=accid) | Q(account2_id=accid))
        transfers_serializer = TransferSerializer(transfers, many=True)
        return Response(transfers_serializer.data)

class MakeTransfer(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TransferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Validation errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
