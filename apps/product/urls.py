from django.urls import path
from .views import products_view, product_view, product_list

urlpatterns = [
    path('', products_view, name='products'),
    path('products/', product_list, name='products_list'),
    path('<int:pk>/', product_view, name='product'),
]
