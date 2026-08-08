import json

from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car):
    serializer = CarSerializer(car)
    json_ = JSONRenderer().render(serializer.data)
    return json_


def deserialize_car_object(json_str: str) -> Car:
    data = json.loads(json_str)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
