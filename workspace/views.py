import email
from functools import partial
from django.shortcuts import render
from .models import User, Task
# from django.shortcuts import render, redirect
from .models import User, Task
from django.http import JsonResponse
from rest_framework import permissions, generics
from .serializers import UserSerializer, TaskSerializer
import json
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .forms import TaskForm, UserForm

class UserList (generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

class TaskCreate(APIView):
    def post(self, request,format = None):
        data = request.data
        tasksCreator = User.objects.get(id=int(data['created_by_id']))
        tasksAssignedto = User.objects.get(email=data.get("tasked_to_email"))
        if tasksCreator is None:
            return Response(
                {'detail': 'tasksCreator not exist'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if tasksAssignedto is None:
            return Response(
                {'detail': 'tasksAssignedto not exist'},
                status=status.HTTP_400_BAD_REQUEST
            )

        newTask = Task.objects.create(
            task_name = data.get('task_name'),
            status = data.get('status'),
            description = data.get('description'),
            taskImgURL = data.get('taskImgURL'),
            created_by_id = tasksCreator,
            tasked_to_id = tasksAssignedto,
        )
        serializer = TaskSerializer(newTask, many=False) 
        return Response(serializer.data,status=status.HTTP_201_CREATED)

# update
class TaskUpdate(APIView):

    def put(self, request, pk):
        # find task in database which has id = pk
        foundTask = Task.objects.filter(id=pk).first()

        serializer = TaskSerializer(foundTask, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# update YuDy
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

     
# Create Yudy

def TaskCreateNew(request):
    # Finding person in charge id
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

# Read Route

def ViewUserTask(request, pk):
    viewTask = Task.objects.get(id=pk)
    return JsonResponse({"result":{"id":viewTask.id,"task_name":newTask.task_name}})


