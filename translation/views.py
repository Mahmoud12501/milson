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
    # def send_email(self,request):
    #     if request.method=='POST':
    #         subject="translate file"
    #         email=request.POST['email']
    #         phone=request.POST['phone']
    #         to=request.POST['t_to']
    #         f_m=request.POST['t_from']
    #         file=request.POST['file']
    #         print(phone)
    #         print(email)
            
            
            
    #         send_mail(
    #             subject,
    #             f"to {to} from {f_m} \n{file} \n{email}\n {phone}",
    #             email,
    #             [settings.EMAIL_HOST_USER]  
                
    #         )

class ViewsetsLanguages(viewsets.ModelViewSet):
    queryset = Languges.objects.all()
    serializer_class = LangugesSerializers
    lookup_field='slug'
    
