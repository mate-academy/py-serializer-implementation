from io import BytesIO

from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    car_serializer = CarSerializer(car)
    return JSONRenderer().render(car_serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    car_bytes = BytesIO(json)
    car_data = JSONParser().parse(car_bytes)
    car_serializer = CarSerializer(data=car_data)
    if car_serializer.is_valid():
        car_serializer.save()
        return Car(**car_serializer.data)

    raise ValidationError("Car data is not valid")
