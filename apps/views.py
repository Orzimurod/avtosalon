from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework.generics import ListAPIView,RetrieveAPIView,ListCreateAPIView

from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


from apps.filters import CarFilter
from apps.models import Car, CarBrand
from apps.serializers import CarBrandSerializers, CarBrandSingleSerializer, CarSerializer

class CarBrandListView(ListAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializers

class BrandDetailView(RetrieveAPIView):
    queryset = CarBrand.objects.all()  
    serializer_class = CarBrandSingleSerializer


class CarsView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['brand', 'name', 'price']
    filterset_class = CarFilter
    

class CarDetailView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
