from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Room
from .serializers import RoomSerializer


import os
from dotenv import load_dotenv
from pathlib import Path


# Create your views here.

@api_view(['GET'])
def RoomView(request):
    queryset =  Room.objects.all()
    serializer = RoomSerializer(queryset, many=True)
    return Response(serializer.data)
