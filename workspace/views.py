import email
from functools import partial
from django.shortcuts import render
from .models import User, Task
# from django.shortcuts import render, redirect
from .models import User, Task
from django.http import JsonResponse
from rest_framework import permissions, generics, status
from .serializers import UserSerializer, TaskSerializer, TokenSerializer
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

class LoginView(generics.ListCreateAPIView):
    """
    POST user/login/
    """

    # This permission class will overide the global permission class setting
    # Permission checks are always run at the very start of the view, before any other code is allowed to proceed.
    # The permission class here is set to AllowAny, which overwrites the global class to allow anyone to have access to login.
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


    def post(self, request, *args, **kwargs):
        email = request.data.get("email", "")
        password = request.data.get("password", "")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            # login saves the user’s ID in the session,
            # using Django’s session framework.
            login(request, user)
            refresh = RefreshToken.for_user(user)
            serializer = TokenSerializer(data={
                # using DRF JWT utility functions to generate a token
                "token": str(refresh.access_token)
                })
            serializer.is_valid()
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class RegisterUsersView(generics.ListCreateAPIView):
    """
    POST user/signup/
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        password = request.data.get("password", "")
        email = request.data.get("email", "")
        role = request.data.get("role", "")
        if not role or not password or not email:
            return Response(
                data={
                    "message": "role, password and email is required to register a user"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        new_user = User.objects.create_user(
            role=role, password=password, email=email
        )
        return Response(status=status.HTTP_201_CREATED)

class UserList (generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticated,)





# update task
def NewTaskUpdate(request, pk):
    # Finding the task that has that ID
    task = Task.objects.get(id=pk)
    # Find the person in charge by their email 
    personInChargeId = User.objects.get(email=request.POST["tasked_to_id"]).pk

    post = request.POST.copy()
    post["tasked_to_id"] = personInChargeId
    request.POST = post

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        print("form:", form.data)
        if form.is_valid():
            updatedTask = form.save()
            return JsonResponse({"result":{"id":updatedTask.id,"task_name":updatedTask.task_name}})
    else:
        form = TaskForm(instance=task)
    return JsonResponse({"status":"Fail to update"})

     
# Create Task

def TaskCreateNew(request):
    # Finding person in charge id
    # Made changes here, added DICT befor GET method ===========>
    personInChargeId = User.objects.get(email=request.POST["tasked_to_id"]).pk
    
    post = request.POST.copy()
    post["tasked_to_id"] = personInChargeId
    request.POST = post

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            newTask = form.save()
            return JsonResponse({"result":{"id":newTask.id,"task_name":newTask.task_name}})
    else:
        form = TaskForm()
    return JsonResponse({"status":"Fail to update"})

# Read Tasks assign to me 

def ViewTaskToMe(request, pk):
    print("========================>", pk)
    task = Task.objects.filter(tasked_to_id=pk)
    print("========================>", task)
    allTasksOfThatPIC= task.values('id', 'task_name', 'status', 'description','taskImgURL','created_by_id','tasked_to_id')
    view_list = list(allTasksOfThatPIC)
    print("========================>", view_list)
    return JsonResponse(view_list, safe=False)

# Read Tasks I create

def ViewTaskCreated(request, pk):

    taskCreated = Task.objects.filter(created_by_id=pk)
    print("========================>", taskCreated)
    showTasksCreated = taskCreated.values('id', 'task_name', 'status','description','taskImgURL','created_by_id','tasked_to_id')
    view_tasks_list = list(showTasksCreated)
    print("========================>", view_tasks_list)
    return JsonResponse(view_tasks_list, safe=False)

def ViewTask(request, pk):
    viewOneTask = Task.objects.get(id=pk)
    print(type(viewOneTask))
    return JsonResponse(model_to_dict(viewOneTask))

def ViewOneUser(request, pk):
    viewOneUser = User.objects.get(id=pk)
    print(type(viewOneUser))
    return JsonResponse(model_to_dict(viewOneUser))


# Delete Route
def DeleteOneTask (request, pk):
    Task.objects.get(id=pk).delete()
    return JsonResponse({"Status":"Task is successfully deleted."})



# # serialize 1 class instance
# def artist_detail2(request,pk):
#   artist = Artist.objects.get(id=pk)
#   print(type(artist))
#   return JsonResponse(model_to_dict(artist))