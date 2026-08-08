import json
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return bytes(json.dumps(serializer.data, separators=(",", ":")), "UTF-8")


def deserialize_car_object(json_bytes: bytes) -> Car:
    json_data = json.loads(json_bytes)
    serializer = CarSerializer(data=json_data)
    if serializer.is_valid():
        return serializer.save()
