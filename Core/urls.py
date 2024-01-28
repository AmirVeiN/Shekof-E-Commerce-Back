from django.contrib import admin
from django.urls import path, include
from product import views

urlpatterns = [
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('product.urls')),
    path('admin/', admin.site.urls),
    path('import/', views.importData),
]
