import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(instance=car)
    return json.dumps(serializer.data, separators=(",", ":")).encode()


def deserialize_car_object(json_data: bytes) -> Car:
    data = json.loads(json_data)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return serializer.save()
    raise ValueError(serializer.errors)
