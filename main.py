import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.serializers import CarSerializer
from car.models import Car


def serialize_car_object(car: Car) -> bytes:
    return JSONRenderer().render(CarSerializer(car).data)


def deserialize_car_object(json: bytes) -> Car:
    pass
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return serializer.save()
