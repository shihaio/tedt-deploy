from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class User (models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.CharField(max_length=75)
  password = models.CharField(max_length=50)
  role = models.CharField(max_length=50)
  birthday = models.DateField()
  user_created_date = models.DateTimeField()

  def __str__(self):
      return self.email

class Task (models.Model):
  task_name = models.CharField(max_length=50)
  status = models.CharField(max_length=25)
  description = models.CharField(max_length=255)
  imgURL = models.CharField(max_length=255)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
  created_date = models.DateField()
  tasked_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")

  
  def __str__(self):
      return self.task_name