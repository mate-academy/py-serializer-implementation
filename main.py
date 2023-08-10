import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from car.serializers import CarSerializer
from car.models import Car


def serialize_car_object(car: Car) -> bytes:
    car_serialize = CarSerializer(car)
    json_data = JSONRenderer().render(car_serialize.data)
    return json_data


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    car_serialize = CarSerializer(data=data)
    if car_serialize.is_valid():
        car = car_serialize.save()
        return car
    return car_serialize.errors
