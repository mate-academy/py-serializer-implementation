import io

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    car_serializer = CarSerializer(car).data
    return JSONRenderer().render(car_serializer)


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer_car = CarSerializer(data=data)
    if serializer_car.is_valid():
        car = serializer_car.save()
        return car

    return serializer_car.errors
