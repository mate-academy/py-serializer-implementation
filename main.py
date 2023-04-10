import json
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json_data: bytes) -> Car:
    data = json.loads(json_data)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        car = serializer.save()
        return car
    else:
        raise serializers.ValidationError(serializer.errors)
