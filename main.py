import io

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from car.serializers import CarSerializer
from car.models import Car


def serialize_car_object(car: Car) -> bytes:
    car_serializer = CarSerializer(car)
    print(car)
    json = JSONRenderer().render(car_serializer.data)
    return json


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    car_data = JSONParser().parse(stream)
    car = Car.objects.create(**car_data)
    return car
