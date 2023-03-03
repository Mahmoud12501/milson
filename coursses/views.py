from django.shortcuts import render
from rest_framework.views import APIView
from.serializer import CoursseSerializers
from .models import Coursse
from rest_framework.response import Response
# Create your views here.
class Coursees_List(APIView):
    def get(self, request):
        coursees = Coursse.objects.all()
        serializer = CoursseSerializers(coursees, many = True)
        return Response(serializer.data)