from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from user.permissions import IsTypeOneUser, IsUser
from sms_ir import SmsIr


class OrderListCreateAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        orders = Order.objects.filter(user=user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
                serializer.save(user=request.user)
                sms_ir = SmsIr(
                "o1Affme8CeJfdW8OuPMv1qo1f1JKDIy0vT7MKLvJvfkF6pgnre2ugXghVeAdQcKz",
                30007732011682,
            )

                sms = sms_ir.send_sms(
                    number=f"+98{request.data["phone"]}",
                    message=f"سلام , سفارش شما ثبت شد",
                )
                return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdminOrderListAPIView(APIView):

    permission_classes = [IsTypeOneUser]

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            pk = request.data["pk"]
            order = Order.objects.get(pk=pk)
            order.status = int(request.data("status"))
            order.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
