import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return json.dumps(serializer.data, serializer=(",", ":")).encode("utf-8")


def deserialize_car_object(json_data: bytes) -> Car:
    data = json.loads(json_data)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    car = Car(**serializer.validated_data)
    car.save()
    return Car(**serializer.validated_data)
