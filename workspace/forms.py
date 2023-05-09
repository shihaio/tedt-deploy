from django import forms
from .models import Task, User

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = (
      "email",
    )
  # def create(self, validated_data):
  #   return User.objects.create_user(**validated_data)
# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = User
#         fields = ('email', )
    
class TaskForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = (
      "task_name",
      "status",
      "description",
      "taskImgURL",
      "created_by_id",
      "tasked_to_id",
    )