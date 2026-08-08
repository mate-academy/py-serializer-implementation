import sys
import os

import json
from car.models import Car
from car.serializers import CarSerializer


sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def serialize_car_object(car: Car) -> str:
    """
    Принимает объект Car и возвращает JSON-представление.
    """
    serializer = CarSerializer(car)
    return json.dumps(serializer.data, separators=(",", ":")).encode("utf-8")


def deserialize_car_object(car_json: str) -> Car:
    """
    Принимает JSON-представление и возвращает экземпляр Car.
    """
    data = json.loads(car_json)
    serializer = CarSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        return serializer.save()
