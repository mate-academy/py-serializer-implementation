import json

from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serialize = CarSerializer(car)
    return JSONRenderer().render(serialize.data)


def deserialize_car_object(json_data: bytes) -> Car:
    data = json.loads(json_data)
    car = CarSerializer(data=data)
    if car.is_valid():
        return car.save()
    else:
        raise car.errors
