import io
from car.models import Car
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    pass
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json_bytes: bytes) -> Car:
    stream = io.BytesIO(json_bytes)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    instance = serializer.save()
    return instance
