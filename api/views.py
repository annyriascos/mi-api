from django.shortcuts import render
from rest_framework import viewsets 
from .models import producto
from .serializers import productoSerializer 

class productoViewSet(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    serializer_class = productoSerializer

# Create your views here.
