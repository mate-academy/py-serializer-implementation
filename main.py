import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return json.dumps(serializer.data, separators=(",", ":")).encode("utf-8")


def deserialize_car_object(car_json: bytes) -> Car:
    car_data = json.loads(car_json)
    serializer = CarSerializer(data=car_data)
    if serializer.is_valid():
        car = Car(**serializer.validated_data)
        car.id = car_data.get("id")
        return car
    else:
        raise ValueError("Invalid car data")
