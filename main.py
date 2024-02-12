import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    car_serializer = CarSerializer(car)
    serialized_data = car_serializer.data
    json_data = json.dumps(serialized_data)
    return json_data.encode()


def deserialize_car_object(json_bytes: bytes) -> Car:
    json_str = json_bytes.decode()
    data_json_str = json.loads(json_str)
    car_serializer = CarSerializer(data=data_json_str)
    if car_serializer.is_valid():
        car_instance = car_serializer.save()
        return car_instance
