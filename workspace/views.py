import email
from functools import partial
from urllib import request
from django.shortcuts import render
from .models import User, Task
# from django.shortcuts import render, redirect
from .models import User, Task
from django.http import JsonResponse
from rest_framework import permissions, generics, status
from .serializers import UserSerializer, TaskSerializer
import json
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .forms import TaskForm, UserForm
from django.forms.models import model_to_dict

# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# JWT settings
from rest_framework_simplejwt.tokens import RefreshToken

# REGISTER
class RegisterUsersView(generics.ListCreateAPIView):

    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        password = request.data.get("password", "")
        
        email = request.data.get("email", "")
        profileURL = request.data.get("profileURL", "")
        if not password or not email:
            return Response(
                data={
                    "message": "Password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            password=password, email=email, profileURL=profileURL
        )
        return Response(status=status.HTTP_201_CREATED)

# LOGOUT
class BlacklistTokenView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        print("======================>request.data",request.data)
        try:
            refresh_token = request.data.get("refresh_token")
            print("======================>refresh_token", refresh_token)
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)



# UPDATE TASK
def NewTaskUpdate(request, pk):
    #find that task inside database, find by id
    targetTask = Task.objects.get(id=pk)
    # print(" ================> pk is:", pk)
    # decode request.body, to access what user send backend
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    # print("===========================> body", body)

    #Find Person, bring them to the save
    personInCharge = User.objects.get(email=body["tasked_to_id"])
    personCreatedTask = User.objects.get(email=body["created_by_id"])

    # start to update Task:
    targetTask.task_name = body["task_name"]
    targetTask.created_by_id = personCreatedTask
    targetTask.tasked_to_id = personInCharge
    targetTask.status = body["status"]
    targetTask.taskImgURL = body["taskImgURL"]
    targetTask.description = body["description"]

    targetTask.save()
    return JsonResponse(model_to_dict(targetTask))
     
# CREATE TASK

def TaskCreateNew(request):
    # Finding person in charge id
    # Made changes here, added DICT befor GET method ===========>
    print("===========================>request.user:", request.user)
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode) 
    # finding person
    personInCharge = User.objects.get(email=body["tasked_to_id"])
    personCreatedTask = User.objects.get(id=body["created_by_id"])
    body["tasked_to_id"] = personInCharge
    body["created_by_id"] = personCreatedTask
    data = Task.objects.create(**body)

    return JsonResponse(model_to_dict(data))


# Read ViewTaskApproved Tasks

def ViewTaskApproved(request):
    approvedTasks = Task.objects.filter(status="APPROVED")
    approvedTasksValue= approvedTasks.values('id', 'task_name', 'status', 'description','taskImgURL','created_by_id','tasked_to_id')
    view_list = list(approvedTasksValue)
    return JsonResponse(view_list, safe=False)

# Read Tasks assign to me 

def ViewTaskToMe(request, pk):
    task = Task.objects.filter(tasked_to_id=pk).exclude(status="APPROVED")
    tasksToPersonInCharge = task.values('id', 'task_name', 'status', 'description','taskImgURL','created_by_id','tasked_to_id')
    view_list = list(tasksToPersonInCharge)
    return JsonResponse(view_list, safe=False)

# Read Tasks I create

def ViewTaskCreated(request, pk):
    taskCreated = Task.objects.filter(created_by_id=pk).exclude(status="APPROVED")
    showTasksCreated = taskCreated.values('id', 'task_name', 'status','description','taskImgURL','created_by_id','tasked_to_id')
    view_tasks_list = list(showTasksCreated)
    return JsonResponse(view_tasks_list, safe=False)

# Read one Task
def ViewTask(request, pk):
    
    viewOneTask = Task.objects.get(id=pk)
    print(viewOneTask)
    return JsonResponse(model_to_dict(viewOneTask))

# Read one User
def ViewOneUser(request, pk):
    viewOneUser = User.objects.get(id=pk)
    print("========================>viewOneUser",viewOneUser.tasks_assignedto)
    return JsonResponse({
        "email":viewOneUser.email, 
        "username": viewOneUser.username,
        "profileURL": viewOneUser.profileURL,
        "role": viewOneUser.role,
        "birthday": viewOneUser.birthday,
        "user_created_date": viewOneUser.user_created_date,
    })

# Update One User Information
def UpdateOneUser(request, pk):
    targetUser = User.objects.get(id=pk)

    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    targetUser.profileURL = body["profileURL"]
    targetUser.role = body["role"]
    targetUser.save()
    return JsonResponse(model_to_dict(targetUser))

# Read Email List Exclude Email of Owner
def ViewEmailList(request, pk):
    emails = User.objects.exclude(id=pk).values('email')
    view_list = list(emails)
    return JsonResponse(view_list, safe=False)

# Delete Task
def DeleteOneTask (request, pk):
    Task.objects.get(id=pk).delete()
    return JsonResponse({"Status":"Task is successfully deleted."})

# Delete User
def DeleteOneUser (request, pk):
    User.objects.get(id=pk).delete()
    return JsonResponse({"Status":"User is successfully deleted."})

#  READ USERLIST 
def UserList(request):
    readUsers= User.objects.values(     
      "id",
      "username",
      "email",
      "password",
      "profileURL",
      "role",
      "birthday",
      "user_created_date", )
    view_list = list(readUsers)
    return JsonResponse(view_list, safe=False)

#  READ TASKLIST
def TaskList(request):
    tasks = Task.objects.values('id', 'task_name', 'status','description','taskImgURL','created_by_id','tasked_to_id')
    view_list = list(tasks)
    return JsonResponse(view_list, safe=False)

