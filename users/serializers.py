from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User
from accounts.serializers import AccountSerializer


class UserSerializer(serializers.ModelSerializer):
    account_owner = AccountSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','account_owner')

class LoginSerializer(serializers.Serializer):
    """
    This serializer defines two fields for authentication:
      * username
      * password.
    It will try to authenticate the user with when validated.
    """
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
    #    attrs['sessionid'] = self.context.get('request').session.session_key
        return attrs


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self,attr):
        username = attr.get('username')
        password = attr.get('password')
        #email = attr.get('email')
        if username and password:
            if User.objects.filter(username=username).exists():
                msg = 'Username already exists.'
                raise serializers.ValidationError(msg, code='authorization')
            user = User.objects.create_user(username=username,password=password)
            user.save()
            usr = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            attr['usr'] = usr
        else:
            msg = 'All fields are required.'
            raise serializers.ValidationError(msg, code='authorization')
        return attr