from rest_framework import serializers
from .models import OrderProduct, Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ("user",)


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ["id", "product", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    products = OrderProductSerializer(many=True, source="orderproduct_set")

    class Meta:
        model = Order
        fields = [
            "id",
            "firstName",
            "lastName",
            "compony",
            "address",
            "postalCode",
            "ostan",
            "city",
            "phone",
            "email",
            "codeMeli",
            "extraText",
            "payType",
            "translateType",
            "products",
            "pay",
            "date",
            "status",
        ]
