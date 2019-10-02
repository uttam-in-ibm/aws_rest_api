from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class SampleGet(APIView):

    def get(self, request, format=None):
        content = {
            "Message":"Hello"
            }
        print("Hello")
        return Response(content,status.HTTP_200_OK)