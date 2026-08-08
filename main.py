from car.serializers import CarSerializer
from car.models import Car
import json


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return json.dumps(serializer.data, separators=(",", ":")).encode("utf-8")


def deserialize_car_object(json_data: bytes) -> Car:
    car_dict = json.loads(json_data.decode("utf-8"))
    serializer = CarSerializer(data=car_dict)

    if serializer.is_valid():
        return serializer.save()
    else:
        raise ValueError(f"Invalid data: {serializer.errors}")
