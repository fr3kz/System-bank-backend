from users.models import User
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate(self,data):
        # Dodaj dowolne niestandardowe walidacje, jeśli są potrzebne
        return data

    def create(self,validated_data):
        employe = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data['username'],
            is_Employee=True,
        )

        return employe


