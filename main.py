from rest_framework import serializers

from car.models import Car
import json
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return json.dumps(serializer.data, separators=(",", ":")).encode("utf-8")


def deserialize_car_object(json_data: bytes) -> Car:
    data = json.loads(json_data.decode("utf-8"))
    serializer = CarSerializer(data=data)

    if serializer.is_valid():
        return Car(**serializer.validated_data)
    else:
        raise serializers.ValidationError(serializer.errors)
