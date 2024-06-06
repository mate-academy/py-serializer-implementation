import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    serialized_data = serializer.data
    json_data = json.dumps(serialized_data, separators=(",", ":"))
    return json_data.encode("utf-8")


def deserialize_car_object(json_bytes: bytes) -> Car:
    json_str = json_bytes.decode("utf-8")
    json_data = json.loads(json_str)
    serializer = CarSerializer(data=json_data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
