from rest_framework import serializers

from user.models import User, PhoneCode


class UserSerializer(serializers.ModelSerializer):

    date_joined = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "phone",
            "date_joined",
            "user_type",
        )

    def get_date_joined(self, obj):
        return obj.date_joined.strftime("%Y-%m-%d %H:%M")


class CodePhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneCode
        fields = ["code", "phone"]
