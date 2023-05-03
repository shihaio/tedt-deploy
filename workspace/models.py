from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class User (models.Model):
  username = models.CharField(max_length=50,null=True)
  email = models.CharField(max_length=75)
  password = models.CharField(max_length=50)
  profileURL = models.CharField(max_length=100,null=True)
  role = models.CharField(max_length=50)
  birthday = models.DateField(null=True)
  user_created_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.email

class Task (models.Model):
  task_name = models.CharField(max_length=50)
  status = models.CharField(max_length=25, default="PENDING")
  description = models.CharField(max_length=255)
  taskImgURL = models.CharField(max_length=255, null=True)
  created_by_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks_creator")
  created_date = models.DateTimeField(auto_now_add=True)
  tasked_to_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks_assignedto")
  
  def __str__(self):
      return self.task_name