from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
#     path('api/v1/auth/token/', jwt_views.TokenObtainPairView.as_view(),
#          name='token_obtain_pair'),
#     path('api/v1/auth/token/refresh/', jwt_views.TokenRefreshView.as_view(),
#          name='token_refresh'),
#     path('api/v1/auth/login/', views.LoginView.as_view(), name="auth-login"),
#     path('api/v1/auth/signup/', views.RegisterUsersView.as_view(), name="user-signup"),
]