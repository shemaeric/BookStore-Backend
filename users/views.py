from django.shortcuts import render
from rest_framework import generics

from . import models
from . import Serializers

class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = Serializers.UserSerializer