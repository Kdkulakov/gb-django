from django.urls import path

from products.endpoint.products import product_list

from products.views.products import (ProductGenericCreate, ProductGenericUpdate, ProductDetail, ProductList, ProductGenericDelete, product_detail)

app_name = 'products'

endpointpatterns = [
    path('api/products/', product_list, name='list_api'),
]

urlpatterns = [
    path('create/', ProductGenericCreate.as_view(), name='create'),
    path('update/<slug:slug>/', ProductGenericUpdate.as_view(), name='update'),
    path('delete/<slug:slug>/', ProductGenericDelete.as_view(), name='delete'),
    path('<slug:slug>/', ProductDetail.as_view(), name='detail'),
    path('', ProductList.as_view(), name='list'),
] + endpointpatterns

