import json

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    car.save()
    return json.dumps(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    data = json.loads(json)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return Car(**serializer.validated_data)
