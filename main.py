from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    car = get_object_or_404(Car, pk=car.pk)
    serializer = CarSerializer(car)
    return Response(serializer.data, status=status.HTTP_200_OK)


def deserialize_car_object(json: bytes) -> Car:
    serializer = CarSerializer(data=json)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
