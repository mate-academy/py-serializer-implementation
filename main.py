from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    if serializer.is_valid():
        return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    data = JSONParser().parse(json)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return serializer.validated_data
