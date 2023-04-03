import io

from django.core.exceptions import ValidationError
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    return JSONRenderer().render(CarSerializer(car).data)


def deserialize_car_object(json_car: bytes) -> Car | ValidationError:
    car_steam = io.BytesIO(json_car)
    car_dict = JSONParser().parse(car_steam)
    car_serializer = CarSerializer(data=car_dict)
    if car_serializer.is_valid():
        return Car(**car_serializer.data)
    return ValidationError("error")

