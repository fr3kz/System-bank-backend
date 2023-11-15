from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
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

#@method_decorator(csrf_exempt, name='dispatch')
class MakeTransfer(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        print(request.data)
        serializer = TransferSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message": "Transfers successful", "transfers": serializer.data},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Transfers failed", "transfers": serializer.data}, status=status.HTTP_400_BAD_REQUEST)