from rest_framework.renderers import JSONRenderer

import json as json_lib

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json_renderer = JSONRenderer()
    json_bytes = json_renderer.render(serializer.data)

    return json_bytes


def deserialize_car_object(json: bytes) -> Car:
    json_data = json_lib.loads(json.decode("utf-8"))
    serializer = CarSerializer(data=json_data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.instance
