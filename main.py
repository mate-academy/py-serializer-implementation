from car.models import Car
from car.serializers import CarSerializer
import json


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json_str = json.dumps(serializer.data, separators=(",", ":"))
    return bytes(json_str, "utf-8")


def deserialize_car_object(jsonn: bytes) -> Car:
    json_str = jsonn.decode("utf-8")
    data = json.loads(json_str)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
