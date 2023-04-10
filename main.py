from rest_framework import serializers
from rest_framework.utils import json
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json_string = json.dumps(serializer.data)
    return json_string.encode("utf-8")


def deserialize_car_object(json: bytes) -> Car:
    serializer = CarSerializer(data=json)
    if serializer.is_valid():
        car = serializer.save()
        return car
    else:
        raise serializers.ValidationError(
            "Invalid data provided for deserialization"
        )
