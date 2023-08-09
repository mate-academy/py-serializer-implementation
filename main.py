import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    serialized_data = serializer.data
    serialized_json = json.dumps(serialized_data)
    return serialized_json.encode("utf-8")


def deserialize_car_object(json_data: bytes) -> Car:
    deserialized_json = json_data.decode('utf-8')
    data = json.loads(deserialized_json)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
