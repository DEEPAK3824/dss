from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import Response
from .models import Documents, Folders ,Topics
from .serializers import dssSerializers

class dsslist(APIView):
    def get(selfself,request):

# Create your views here.
