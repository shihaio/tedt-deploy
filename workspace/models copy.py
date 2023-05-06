# from pyexpat import model
# from unittest.util import _MAX_LENGTH
# from django.db import models
# from django.conf import settings
# import json
# # from django.conf import settings
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# from django.utils import timezone
# from django.utils.translation import gettext_lazy as _

# class CustomAccountManager(BaseUserManager):

#     def create_superuser(self, email, password, **other_fields):

#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)
#         other_fields.setdefault('is_active', True)

#         if other_fields.get('is_staff') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_staff=True.')
#         if other_fields.get('is_superuser') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_superuser=True.')

#         return self.create_user(email, password, **other_fields)

#     def create_user(self, email, password, **other_fields):

#         if not email:
#             raise ValueError(_('You must provide an email address'))

#         email = self.normalize_email(email)
#         user = self.model(email=email,  **other_fields)
#         user.set_password(password)
#         user.save()
#         return 

# # Create your models here.
# class User (AbstractBaseUser, PermissionsMixin):
#   username = models.CharField(max_length=50,null=True)
#   email = models.EmailField(verbose_name="email", max_length=50, unique=True)
#   # email, maybe i can use EmailField()
#   # password = models.CharField(max_length=10)
#   profileURL = models.CharField(max_length=100,null=True)
#   role = models.CharField(max_length=50)
#   birthday = models.DateField(null=True)
#   user_created_date = models.DateTimeField(auto_now_add=True)
#   is_admin = models.BooleanField(default=False)
#   is_active = models.BooleanField(default=False)
#   is_staff = models.BooleanField(default=False)
#   is_superuser = models.BooleanField(default=False)

#   objects = CustomAccountManager()

#   USERNAME_FIELD = 'email'
# #   REQUIRED_FIELDS = ['role']

#   def __str__(self):
#       return self.email

# class Task (models.Model):
#   task_name = models.CharField(max_length=50)
#   status = models.CharField(max_length=25, default="PENDING")
#   description = models.CharField(max_length=255)
#   taskImgURL = models.CharField(max_length=255, null=True)
#   created_by_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tasks_creator")
#   created_date = models.DateTimeField(auto_now_add=True)
#   tasked_to_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tasks_assignedto")


#   def toJson(self):
#         return json.dumps(self, default=lambda o: o.__dict__, 
#             sort_keys=True, indent=4)

#   def __str__(self):
#       return self.task_name


