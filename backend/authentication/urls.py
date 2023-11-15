from django.urls import path
from .views import RegisterView, PasswordCreationView, LoginView, AuthStatusView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register_user'),
    path('password/<str:token>/', PasswordCreationView.as_view(), name='password_creation'),

    path('status/', AuthStatusView.as_view(), name='auth_status')
]
