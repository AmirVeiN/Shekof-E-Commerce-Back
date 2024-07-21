from django.db import models
from user.models import User, Adresses
from product.models import Product
from . import constants as user_constants


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    compony = models.CharField(max_length=50, blank=True, null=True)
    address = models.ForeignKey(Adresses, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    codeMeli = models.CharField(max_length=50)
    extraText = models.TextField(max_length=500, blank=True, null=True)
    payType = models.PositiveSmallIntegerField(choices=user_constants.USER_TYPE_CHOICES)
    translateType = models.PositiveSmallIntegerField(
        choices=user_constants.USER_TRANSLATE_CHOICES
    )
    products = models.ManyToManyField(Product, through="OrderProduct")
    pay = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField(
        choices=user_constants.ORDER_CHOICES, default=1
    )

    def __str__(self):
        return f"{self.user} -- {self.address}"


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()  # تعداد محصول

    def __str__(self):
        return f"{self.order} -- {self.product} -- {self.quantity}"
