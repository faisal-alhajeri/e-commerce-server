from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_cart_items),
    path('add/', views.add_to_cart),
    path('delete/', views.delete_from_cart),
    path('increment/', views.increment_cart),
    path('decrement/', views.decrement_cart),
]