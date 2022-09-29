from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products_view),
    path('<uuid:product_uuid>/', views.single_products_view),
    path('categories/', views.all_products_categories),
    path('create/', views.create_product),
    path('<uuid:product_uuid>/delete/', views.delete_product),
    path('<uuid:product_uuid>/update/', views.update_product),
    path('image/<uuid:image_uuid>/delete/', views.delete_product_image),
]
