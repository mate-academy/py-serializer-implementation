import io

from rest_framework.exceptions import ValidationError
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from car.serializers import CarSerializer
from car.models import Car


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        instance = serializer.save()
        return instance

    else:
        raise ValidationError(serializer.errors)
