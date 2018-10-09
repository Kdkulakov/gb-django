from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
    path('get_template/', views.get_list_template),
    path('render_to_string/', views.render_list_to_string),
    path('native/', views.native),
    path('create/', views.product_create, name='create'),
    path('categories/create/', views.category_create, name='category_create'),
    path('update/<slug:title>/', views.product_update, name='update'),
    path('<slug:title>/', views.product_detail, name='detail'),
    path('', views.product_list, name='list'),
]
