from django.shortcuts import render
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework import generics


class CustomUserAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

