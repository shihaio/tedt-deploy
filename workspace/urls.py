from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
)


urlpatterns = [
  path('api/v1/users', views.UserList.as_view(), name="user_list"),
  # path('api/v1/user/<int:pk>', views.user_detail.as_view(), name="user-detail"),
  # path('api/v1/user/<int:pk>/edit', views.user_edit.as_view(), name="user_edit"),
  # path('api/v1/user/<int:pk>/delete', views.user_edit.as_view(), name="user_delete"),
  path('api/v1/task/new', views.TaskCreateNew, name="taskNew"),
  path('api/v1/task/read/<int:pk>', views.ViewTask, name="viewTask"),
  path('api/v1/task/<int:pk>', views.NewTaskUpdate, name="taskUpdate"),
  path('api/v1/task/pic/<int:pk>', views.ViewTaskToMe, name="viewTaskToMe"),
  path('api/v1/task/createdBy/<int:pk>', views.ViewTaskCreated, name="viewTaskCreated"),
  path('api/v1/task/delete/<int:pk>', views.DeleteOneTask, name="deleteOneTask"),
  path('api/v1/user/read/<int:pk>', views.ViewOneUser, name="viewOneUser"),
  path('api/v1/user/detail/<int:pk>', views.ReadUserDetail.as_view(), name="user-detail"),
  # path('api/v1/user/read/<int:pk>', views.ViewOneUser, name="viewOneUser"),
  # Authentication
  path('api/v1/auth/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/v1/auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
  path('api/v1/auth/login/', views.LoginView.as_view(), name="auth-login"),
  path('api/v1/auth/signup/', views.RegisterUsersView.as_view(), name="user-signup"),
]