import json as py_json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json_data = py_json.dumps(
        serializer.data,
        separators=(",", ":")
    )
    return json_data.encode("utf-8")


def deserialize_car_object(json_bytes: bytes) -> Car:
    json_str = json_bytes.decode("utf-8")
    data = py_json.loads(json_str)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    car = Car(**serializer.validated_data)
    car.id = data.get("id")
    return car
