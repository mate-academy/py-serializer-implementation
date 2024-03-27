import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serialized_car = CarSerializer(car)
    json = JSONRenderer().render(data=serialized_car.data)
    return json


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    parsed_car_data = JSONParser().parse(stream)
    return Car.objects.create(**parsed_car_data)
