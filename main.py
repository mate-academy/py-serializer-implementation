from rest_framework.parsers import JSONParser

from car.models import Car
from car.serializers import CarSerializer
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
import io


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> CarSerializer:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid()
    return serializer.save()


print(serialize_car_object(Car.objects.create(
    manufacturer="Porsche",
    model="Panamera",
    horse_powers=1234,
    is_broken=False,
)))
