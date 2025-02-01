from io import BytesIO

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    return JSONRenderer(
    ).render(CarSerializer(car).data)


def deserialize_car_object(json: bytes) -> Car:
    stream = BytesIO(json)
    data = JSONParser().parse(stream)
    car = CarSerializer(data=data)
    if car.is_valid():
        car = Car.objects.create(**car.validated_data)
        return car
