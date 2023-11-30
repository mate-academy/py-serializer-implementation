import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.serializers import ValidationError

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    json = JSONRenderer().render(data=serializer.data)

    return json


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream=stream)
    serializer = CarSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Car.objects.get(id=data["id"])

    raise ValidationError(detail=serializer.errors)
