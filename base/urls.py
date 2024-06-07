from django.urls import path
from .views import getProduct, createProduct

urlpatterns = [
    path('products/', getProduct, name="products"),
    path('product-create/', createProduct, name="product-create"),

]
