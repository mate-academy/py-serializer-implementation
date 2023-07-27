import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    pass
    car_serializer = CarSerializer(car)
    json = JSONRenderer().render(car_serializer.data)
    print(json)
    return json


def deserialize_car_object(json: bytes) -> Car:
    pass
    stream = io.BytesIO(json)
    car_data = JSONParser().parse(stream)
    car_instance = Car.objects.create(**car_data)
    return car_instance
