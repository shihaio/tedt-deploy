from rest_framework import serializers
from .models import User, Task
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = (
      "id",
      "username",
      "email",
      "password",
      "profileURL",
      "role",
      "birthday",
      "user_created_date",
      "tasks_creator",
      "tasks_assignedto"
    )
    depth = 1

class TaskSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Task
    fields = (
      "id",
      "task_name",
      "status",
      "description",
      "taskImgURL",
      "created_by_id",
      "created_date",
      "tasked_to_id",
    )
    depth = 1

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)

    token['email'] = user.email
    token['user_id'] = str(user.id)
    token['profileURL'] = user.profileURL
    token['role'] = user.role
    return token

class CustomObtainTokenPairView(TokenObtainPairView):
  serializer_class = CustomTokenObtainPairSerializer