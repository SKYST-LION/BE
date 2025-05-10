from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()

class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'nickname')

    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            nickname = validated_data.get('nickname', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class UserLoginSerialzer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            raise serializers.ValidationError("아이디와 비밀번호를 모두 입력해주세요.")

        user = authenticate(username = email, password=password)

        if not user:
            raise serializers.ValidationError("아이디 또는 비밀번호가 올바르지 않음")

        data["user"] = user
        return data
    
class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "nickname")
