import io
from car.models import Car
from car.serializers import CarSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import ValidationError


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json_data = JSONRenderer().render(serializer.data)
    return json_data


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)

    car_serializer = CarSerializer(data=data)
    if car_serializer.is_valid():
        car_instance = car_serializer.save()
        return car_instance
    else:
        raise ValidationError(car_serializer.errors)
