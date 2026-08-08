import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serialized_car = CarSerializer(instance=car).data
    result_str = json.dumps(serialized_car, separators=(",", ":"))
    return result_str.encode("utf-8")


def deserialize_car_object(json_bytes: bytes) -> Car:
    json_string = json_bytes.decode("utf-8")
    dict_object = json.loads(json_string)
    deserialize_car = CarSerializer(data=dict_object)
    deserialize_car.is_valid(raise_exception=True)
    return deserialize_car.save()
