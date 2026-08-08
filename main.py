from rest_framework.renderers import JSONRenderer
from rest_framework.utils import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    serialized_car = serializer.data
    return JSONRenderer().render(serialized_car)


def deserialize_car_object(json_data: bytes) -> Car:
    car_data = json.loads(json_data)
    serializer = CarSerializer(data=car_data)
    serializer.is_valid(raise_exception=True)
    car = serializer.save()
    return car
