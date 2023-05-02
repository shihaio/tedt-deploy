from django.shortcuts import render
from .models import User, Task
# from django.shortcuts import render, redirect
from .models import User, Task
from django.http import JsonResponse
from rest_framework import permissions, generics
from .serializers import UserSerializer

class UserList (generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

# class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer
#     permission_classes = (permissions.IsAuthenticated,)

    