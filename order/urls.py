from django.urls import path
from .views import OrderListCreateAPIView, AdminOrderListAPIView

urlpatterns = [
    path("orders/", OrderListCreateAPIView.as_view()),
    path("admin/orders/", AdminOrderListAPIView.as_view()),
]
