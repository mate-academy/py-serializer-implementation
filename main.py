from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(Car)
    return JSONRenderer.render(data=serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    data = JSONParser.parse(json)
    return data
