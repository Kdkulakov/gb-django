from django.urls import path

from products.views.categories import CategoryCreate, CategoryDetail, CategoryUpdate, CategoryDelete

app_name = 'categories'

urlpatterns = [
    path('create/', CategoryCreate.as_view(), name='create'),
    path('<slug:slug>/', CategoryDetail.as_view(), name='list'),
    path('update/<slug:slug>/', CategoryUpdate.as_view(), name='update'),
    path('delete/<slug:slug>/', CategoryDelete.as_view(), name='delete')
]
