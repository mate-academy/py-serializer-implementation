from car.models import Car
from car.serializers import CarSerializer
import json as py_json


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return (py_json.dumps(serializer.data, separators=(",", ":"))
            .encode("utf-8"))


def deserialize_car_object(json_bytes: bytes) -> Car:
    data = py_json.loads(json_bytes.decode("utf-8"))
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return Car(**serializer.validated_data)
