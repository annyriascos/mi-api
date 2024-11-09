# serializers.py

from .models import producto
from rest_framework.serializers import ModelSerializer

class productoSerializer(ModelSerializer):
    class Meta:
        model = producto 
        fields = ['id','nombre','descripcion','precio','en_stock']
        