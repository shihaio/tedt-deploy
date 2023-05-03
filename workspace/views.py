from django.shortcuts import render
from .models import User, Task
# from django.shortcuts import render, redirect
from .models import User, Task
from django.http import JsonResponse
from rest_framework import permissions, generics
from .serializers import UserSerializer, TaskSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class UserList (generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

class TaskCreate(APIView):
    serializer_class = TaskSerializer
    # queryset = Task.objects.all()
    # permission_classes = (permissions.AllowAny,)
    def post(self, request,format = None):
        data = request.data
        # Find person has email of "task_to_email" .get('username')
        taskedToPersonId = User.objects.values_list("id",flat=True).get(email=request.data.get("tasked_to_email"))
        newTask = Task.objects.create(
            task_name = data.get('task_name'),
            status = data.get('status'),
            description = data.get('description'),
            imgURL = data.get('imgURL'),
            created_by_id = int(data.get('created_by_id')),
            tasked_to_id = taskedToPersonId,
        )
        serializer = TaskSerializer(newTask, many=False) 
        return Response(serializer.data,status=status.HTTP_201_CREATED)

# update