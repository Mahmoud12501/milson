from django.shortcuts import render
from .serializer import TranslateSerializers,LangugesSerializers
from .models import TranslateDb,Languges
from rest_framework import generics, mixins, viewsets
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


class mixins_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = TranslateDb.objects.all()
    serializer_class = TranslateSerializers
    
    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
   

class ViewsetsLanguages(viewsets.ModelViewSet):
    queryset = Languges.objects.all()
    serializer_class = LangugesSerializers
    lookup_field='slug'
    
