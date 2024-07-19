from rest_framework import serializers
from order.serializers import OrderSerializer
from user.models import Adresses, User, PhoneCode


class UserSerializer(serializers.ModelSerializer):

    date_joined = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "phone",
            "email",
            "codeMeli",
            "first_name",
            "last_name",
            "date_joined",
            "user_type",
        )

    def get_date_joined(self, obj):
        return obj.date_joined.strftime("%Y-%m-%d %H:%M")


class CodePhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneCode
        fields = ["code", "phone"]


class AccessTokenSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()


class UserFillSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "email",
            "codeMeli",
            "first_name",
            "last_name",
            "shaba",
        )


class CreateAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adresses
        fields = ["user", "id", "ostan", "shahr", "adress", "postalCode"]

    def create(self, validated_data):
        user = self.context["request"].user
        address = Adresses.objects.create(user=user, **validated_data)
        return address


class AdminUserSerializer(serializers.ModelSerializer):
    date_joined = serializers.SerializerMethodField()
    addresses = CreateAddressSerializer(
        many=True, read_only=True, source="adresses_set"
    )
    orders = OrderSerializer(many=True, read_only=True, source="order_set")

    class Meta:
        model = User
        fields = (
            "id",
            "phone",
            "email",
            "codeMeli",
            "first_name",
            "last_name",
            "date_joined",
            "user_type",
            "addresses",
            "orders",
        )

    def get_date_joined(self, obj):
        return obj.date_joined.strftime("%Y-%m-%d %H:%M")
