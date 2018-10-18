from django.urls import path

from products.views.products import (ProductGenericCreate, ProductGenericUpdate, ProductDetail, ProductList, ProductDelete)

app_name = 'products'

urlpatterns = [
    path('create/', ProductGenericCreate.as_view(), name='create'),
    path('update/<slug:slug>/', ProductGenericUpdate.as_view(), name='update'),
    path('delete/<slug:slug>/', ProductDelete.as_view(), name='delete'),
    path('<slug:slug>/', ProductDetail.as_view(), name='detail'),
    path('', ProductList.as_view(), name='list'),
]
