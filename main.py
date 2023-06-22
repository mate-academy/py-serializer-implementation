import json
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json_data = serializer.data
    json_bytes = json.dumps(
        json_data, separators=(",", ":")
    ).encode("utf-8")
    return json_bytes


def deserialize_car_object(
        json_bytes: bytes
) -> Car:
    json_data = json_bytes.decode("utf-8")
    data = json.loads(json_data)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
