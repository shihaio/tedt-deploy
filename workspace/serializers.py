from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = (
      "id",
      "first_name",
      "last_name",
      "email",
      "password",
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
      "imgURL",
      "created_by_id",
      "created_date",
      "tasked_to_id",
    )
    depth = 1