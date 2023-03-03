from rest_framework import serializers
from .models import Coursse

class CoursseSerializers(serializers.ModelSerializer):
    class Meta:
        model=Coursse
        fields=['name','description','price','image','slug']
        