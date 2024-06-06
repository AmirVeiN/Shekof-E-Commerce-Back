from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/v1/", include("djoser.urls")),
    path("api/v1/", include("djoser.urls.jwt")),
    path("api/v1/", include("product.urls")),
    path("api/v1/", include("user.urls")),
    path("admin/", admin.site.urls),
]
