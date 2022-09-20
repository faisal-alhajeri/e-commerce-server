from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products_view),
    path('req/', views.all_products_login_view)
]
