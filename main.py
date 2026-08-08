from car.models import Car
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    return JSONRenderer().render(CarSerializer(car).data)


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    return Car(**JSONParser().parse(stream))
