from django.urls import path
from .views import RegisterView, PasswordCreationView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', RegisterView.as_view(), name='register_user'),
    path('password/<str:token>/', PasswordCreationView.as_view(), name='password_creation')
]
