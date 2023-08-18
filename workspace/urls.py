from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
)
from .serializers import UserSerializer, TaskSerializer, TokenSerializer,CustomObtainTokenPairView

urlpatterns = [
  path('api/v1/task/new', views.TaskCreateNew, name="taskNew"),
  path('api/v1/task/read/<int:pk>', views.ViewTask, name="viewTask"),
  path('api/v1/task/<int:pk>', views.NewTaskUpdate, name="taskUpdate"),
  path('api/v1/task/person-in-charge/<int:pk>', views.ViewTaskToMe, name="viewTaskToMe"),
  path('api/v1/task/approved', views.ViewTaskApproved, name="ViewTaskApproved"),
  path('api/v1/task/createdBy/<int:pk>', views.ViewTaskCreated, name="viewTaskCreated"),
  path('api/v1/task/delete/<int:pk>', views.DeleteOneTask, name="deleteOneTask"),

  
  path('api/v1/user/read/<int:pk>', views.ViewOneUser, name="viewOneUser"),
  path('api/v1/user/update/<int:pk>', views.UpdateOneUser, name="updateOneUser"),
  path('api/v1/user/emailList/<int:pk>', views.ViewEmailList, name="viewEmailList"),
  
  # Authentication
  # path('api/v1/auth/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/v1/auth/token/', CustomObtainTokenPairView.as_view(), name='token_obtain_pair'),
  path('api/v1/auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
  path('api/v1/auth/signup/', views.RegisterUsersView.as_view(), name="user-signup"),
  path('api/v1/auth/logout/blacklist/', views.BlacklistTokenView.as_view(), name='blacklist'),
  
  
  # For Admin
  path('api/v1/users', views.UserList, name="user_list"),
  path('api/v1/tasks', views.TaskList, name="task_list"),
  path('api/v1/user/delete/<int:pk>', views.DeleteOneUser, name="deleteOneUser"),

]