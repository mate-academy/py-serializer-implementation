from io import BytesIO

from rest_framework.exceptions import ValidationError
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(
        instance=car
    )
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    json = JSONParser().parse(BytesIO(json))
    serializer = CarSerializer(
        data=json
    )
    if serializer.is_valid():
        serializer.save()
        return serializer.instance
    else:
        raise ValidationError(serializer.errors)
