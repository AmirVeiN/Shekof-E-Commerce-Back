from django.urls import path, include

from product import views

urlpatterns = [
    path('latest-product/', views.LatestProductsList.as_view()),
    path('category-product/<str:category>', views.CategoryProduct.as_view()),
    path('products/sell', views.SellProduct.as_view()),
    path('products/bestSell', views.BestSell.as_view()),
    path('products/new', views.LatestProductsList.as_view()),
    path('products/<str:product_slug>', views.ProductSlug.as_view()),
    
    # path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
]