from django.urls import path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from authentication.views import MyTokenObtainPairView, register_view

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', register_view, name='register'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]