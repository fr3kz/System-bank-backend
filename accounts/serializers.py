from datetime import datetime

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
        # Dodaj dowolne niestandardowe walidacje, jeśli są potrzebne
        account1 = Account.objects.get(account_number=data['account1_id'])
        account2 = Account.objects.get(account_number=data['account2_id'])
        if account1.account_balance < data['amount']:
            raise serializers.ValidationError("Not enough money on account")
        if account1.account_number == account2.account_number:
            raise serializers.ValidationError("You can't transfer money to the same account")

        return data

    def create(self, validated_data):
        # Pobierz dane z validated_data i utwórz obiekt Transfer
        account1_id = validated_data['account1_id']
        account2_id = validated_data['account2_id']
        amount = validated_data['amount']
        title = validated_data['title']

        transfer = Transfer.objects.create(
            account1_id=account1_id,
            account2_id=account2_id,
            amount=int(amount),
            title=title,
            date=datetime.now()
        )
        return transfer