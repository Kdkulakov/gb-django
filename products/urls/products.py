from django.urls import path

from products.views.products import (product_create, product_update, product_detail, product_list)

app_name = 'products'

urlpatterns = [
    path('create/', product_create, name='create'),
    path('update/<slug:title>/', product_update, name='update'),
    path('<slug:title>/', product_detail, name='detail'),
    path('', product_list, name='list'),
]
