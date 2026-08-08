import json as json_module
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return json_module.dumps(
        serializer.data, separators=(",", ":")
    ).encode("utf-8")


def deserialize_car_object(json: bytes) -> Car:
    data = json_module.loads(json)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
