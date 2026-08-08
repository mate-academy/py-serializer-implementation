import json
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return json.dumps(serializer.data, separators=(",", ":")).encode("utf-8")


def deserialize_car_object(car_json: str) -> Car:
    data = json.loads(car_json)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
