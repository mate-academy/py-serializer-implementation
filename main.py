from car.models import Car
import json

from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    data = serializer.data
    return json.dumps(data, separators=(",", ":")).encode("UTF-8")


def deserialize_car_object(json_data: bytes) -> Car:
    data = json.loads(json_data)
    serializer = CarSerializer(data=data)
    serializer.is_valid()
    car = Car(**serializer.validated_data)
    return car
