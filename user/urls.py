from django.urls import path, include
from . import views

urlpatterns = [
    path("phone/send/", views.SendCode.as_view()),
    path("user/create/", views.CreateUser.as_view()),
    path("user/fill/information/", views.FillInformation.as_view()),
    path("user/me/", views.UserInformation.as_view()),
    path("user/address/", views.CreateAddress.as_view()),
    path("user/allusers/", views.GetAllUsers.as_view()),
]
