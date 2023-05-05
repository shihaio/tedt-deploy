from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = (
      "id",
      "username"
      "email",
      "password",
      "profileURL",
      "role",
      "birthday",
      "user_created_date",
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
