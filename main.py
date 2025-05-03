import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json_data = json.dumps(serializer.data, separators=(",", ":"))
    return bytes(json_data, "utf-8")


def deserialize_car_object(json_data: bytes) -> Car:
    data = json.loads(json_data.decode("utf-8"))
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)

    car = Car(**serializer.validated_data)
    return car
