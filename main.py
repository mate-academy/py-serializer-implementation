import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    if serializer.is_valid():
        json = JSONRenderer().render(serializer.data)
        return json


def deserialize_car_object(json: bytes) -> Car:
    serializer = CarSerializer(json)
    data = JSONParser().parse(serializer)
    return data
