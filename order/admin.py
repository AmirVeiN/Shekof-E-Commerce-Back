from django.contrib import admin

from .models import Order, OrderProduct


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1  # تعداد فرم های اضافی خالی که باید نمایش داده شود


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "pay", "date", "status")
    list_filter = ("status", "date")
    search_fields = ("user__username", "user__email", "firstName", "lastName")
    inlines = [OrderProductInline]


admin.site.register(OrderProduct)
