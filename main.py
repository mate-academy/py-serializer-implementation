from car.models import Car
from car.serializers import CarSerializer
import json


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    serialized_data = serializer.data
    json_data = json.dumps(serialized_data, separators=(",", ":"))
    return json_data.encode("utf-8")


def deserialize_car_object(json_data: bytes) -> Car:
    json_str = json_data.decode("utf-8")
    deserialized_data = json.loads(json_str)
    serializer = CarSerializer(data=deserialized_data)
    serializer.is_valid(raise_exception=True)
    car_instance = serializer.save()
    return car_instance
