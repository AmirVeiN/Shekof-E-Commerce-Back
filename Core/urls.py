from django.contrib import admin
from django.urls import path, include
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('import/', views.importData),
    path('api/v1/', include('product.urls')),
    
]
