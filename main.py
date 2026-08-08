from json import loads, dumps

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return dumps(serializer.data, separators=(",", ":")).encode("utf-8")


def deserialize_car_object(json: bytes) -> Car:
    car_json = loads(json)
    serializer = CarSerializer(data=car_json)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
