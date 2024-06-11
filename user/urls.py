from django.urls import path, include
from . import views

urlpatterns = [
    path("phone/send/", views.SendCode.as_view()),
    path("user/create/", views.CreateUser.as_view()),
    path("user/fill/information/", views.FillInformation.as_view()),
]
