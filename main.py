import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return json.dumps(serializer.data, separators=(",", ":")).encode()


def deserialize_car_object(jsons: bytes) -> Car:
    load_json = json.loads(jsons)
    serializer = CarSerializer(data=load_json)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
