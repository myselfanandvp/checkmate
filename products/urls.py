from django.urls import path
from .views import CreateProduct,ListProduct,EditProduct,DeleteProduct
urlpatterns=[
    path('create/',CreateProduct.as_view(),name="createproducturl"),
    path('list/',ListProduct.as_view(),name="listproducturl"),
    path('edit/<int:product_id>/',EditProduct.as_view(),name="editproducturl"),
    path('delete/<int:product_id>/',DeleteProduct.as_view(),name="deleteproducturl"),
]
