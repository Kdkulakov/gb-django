from django.urls import path

from products.views.products import (ProductGenericCreate, ProductGenericUpdate, ProductDetail, ProductList, ProductDelete)

app_name = 'products'

urlpatterns = [
    path('create/', ProductGenericCreate.as_view(), name='create'),
    path('update/<int:pk>/', ProductGenericUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='delete'),
    path('<int:pk>/', ProductDetail.as_view(), name='detail'),
    path('', ProductList.as_view(), name='list'),
]
