import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return JSONRenderer().render(serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    json = io.BytesIO(json)
    data = JSONParser().parse(json)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        car = serializer.save()
        return car
