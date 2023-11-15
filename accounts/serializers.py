from datetime import datetime
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Account,Transfer

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'



class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'

    def validate(self, data):
        print("Validating data:", data)

        account1 = get_object_or_404(Account, account_number=data['account1_id'])
        account2 = get_object_or_404(Account, account_number=data['account2_id'])
        amount = data['amount']
        title = data['title']

        print("Account 1 balance:", account1.account_balance)
        print("Transfer amount:", amount)

        if account1.account_balance < amount:
            raise serializers.ValidationError("Not enough money on account")

        if account1.account_number == account2.account_number:
            raise serializers.ValidationError("You can't transfer money to the same account")

        if amount < 0:
            raise serializers.ValidationError("You can't transfer a negative amount of money")

        if account1.account_balance - amount < 0:
            raise serializers.ValidationError("Transaction would result in a negative balance")

        return data

    def save(self):
        print("jestem tu")
        print("jestem t")
        account1_id = self.validated_data['account1_id']
        account2_id = self.validated_data['account2_id']
        amount = self.validated_data['amount']
        title = self.validated_data['title']

        account1 = get_object_or_404(Account, account_number=account1_id)
        account2 = get_object_or_404(Account, account_number=account2_id)

        account1.account_balance -= amount
        account2.account_balance += amount

        account2.save()
        account1.save()

        transfer = Transfer.objects.create(
            account1_id=account1_id,
            account2_id=account2_id,
            amount=amount,
            title=title,
            date=datetime.now()
        )

        return transfer
