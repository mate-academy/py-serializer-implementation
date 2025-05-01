import json as json_module

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    result = json_module.dumps(serializer.data, separators=(",", ":"))
    return result.encode("utf-8")


def deserialize_car_object(json: bytes) -> Car:
    decoded_data = json.decode("utf-8")
    data = json_module.loads(decoded_data)
    result = Car(**data)
    return result
