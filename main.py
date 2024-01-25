from rest_framework.utils import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    serialized_data = serializer.data
    json_str = json.dumps(serialized_data)
    serialized_bytes = json_str.encode('utf-8')

    return serialized_bytes


def deserialize_car_object(json_data: bytes) -> Car:
    json_file = json_data.decode('utf-8')
    deserialized_data = json.loads(json_file)
    serializer = CarSerializer(data=deserialized_data)
    if serializer.is_valid(raise_exception=False):
        return serializer.save()
    else:
        return None

