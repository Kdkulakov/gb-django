from django.urls import path

from products.views.products import (ProductGenericCreate, ProductGenericUpdate, product_detail, product_list)

app_name = 'products'

urlpatterns = [
    path('create/', ProductGenericCreate.as_view(), name='create'),
    path('update/<slug:pk>/', ProductGenericUpdate.as_view(), name='update'),
    path('<slug:title>/', product_detail, name='detail'),
    path('', product_list, name='list'),
]
