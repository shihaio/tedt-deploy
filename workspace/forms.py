from django import forms
from .models import Task, User

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = (
      "username",
      "profileURL",
    )
    
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