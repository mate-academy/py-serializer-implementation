import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    car_data_json = JSONRenderer().render(serializer.data)
    return car_data_json


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    car_data = JSONParser().parse(stream)
    serializer = CarSerializer(data=car_data)
    serializer.is_valid()
    serializer.save()
    return serializer.instance
