from django.shortcuts import render

from app.models import Producto
from rest_framework import viewsets
from app.models import *
from .serializers import *

class ProductoViewSet(viewsets.ModelViewSet):
    queryset= Producto.objects.all()
    serializer_class = ProductoSerializer
