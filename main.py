import io
from django.db.models import QuerySet
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    if isinstance(car, QuerySet):
        serializer = CarSerializer(car, many=True)
    else:
        serializer = CarSerializer(car)
    json = JSONRenderer().render(serializer.data)
    return json


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Car.objects.get(id=data["id"])
    return serializer.errors
