from django.urls import path, include
from . import views

urlpatterns = [
    path("phone/send/", views.PhoneConfirm.as_view()),
    path("phone/check/", views.CheckPhone.as_view()),
    path("user/create/", views.CreateUser.as_view()),
    path("user/password/forget/", views.PasswordForget.as_view()),
]
