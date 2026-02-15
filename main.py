from json import loads

from rest_framework.renderers import JSONRenderer
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json = JSONRenderer().render(serializer.data)
    return json


def deserialize_car_object(json: bytes) -> Car:
    payload = loads(json.decode("utf-8"))
    serializer = CarSerializer(data=payload)
    serializer.is_valid(raise_exception=True)
    car = serializer.save()
    return car
