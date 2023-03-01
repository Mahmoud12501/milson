from rest_framework import serializers
from .models import TranslateDb ,Languges

class TranslateSerializers(serializers.ModelSerializer):
    class Meta:
        model=TranslateDb
        fields=['t_from','t_to','file','word_count','phone','email']
        
class LangugesSerializers(serializers.ModelSerializer):
    class Meta:
        model=Languges
        fields=['languge']