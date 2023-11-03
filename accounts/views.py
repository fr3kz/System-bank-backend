from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
import datetime
from users.models import User
from .models import Account,Transfer
from .serializers import AccountSerializer,TransferSerializer
from .forms import MakeTransferForm
# Create your views here.
class AccountList(APIView):
   # permission_classes = (permissions.AllowAny,)
    def get(self,request,usrid):
        # do stestowania czy pojdzie user = request.user
        user = User.objects.get(id=usrid)
        Accounts = Account.objects.get(account_owner=user,is_Main=True)
        accout_serializer = AccountSerializer(Accounts,many=False)
        return Response(accout_serializer.data)

class ShowTransferHistory(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, accid):
        transfers = Transfer.objects.filter(Q(account1_id=accid) | Q(account2_id=accid))
        transfers_serializer = TransferSerializer(transfers, many=True)
        return Response(transfers_serializer.data)


class MakeTransfer(APIView):
   # permission_classes = (permissions.AllowAny,)

    def post(self,request):

        form = MakeTransferForm(request.POST)

        if form.is_valid():
            account1 = Account.objects.get(account_number=form.cleaned_data['sender'])
            account2 = Account.objects.get(account_number=form.cleaned_data['receiver'])
            amount = form.cleaned_data['amount']
            if account1.account_balance < amount:
                return Response({'error':'Not enough money on account'},status=400)
            else:
                account1.account_balance -= amount
                account2.account_balance += amount
                account1.save()
                account2.save()
                transfer = Transfer(account1_id=account1.account_number,account2_id=account2.account_number,amount=amount,date=datetime.datetime.now())
                transfer.save()
                return Response({'success':'Transfer completed'},status=200)
        else:
            return Response({'error':'Invalid form'},status=400)

