import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serialize = CarSerializer(car)
    return JSONRenderer().render(serialize.data) if serialize.is_valid else ""


def deserialize_car_object(json: bytes) -> Car:
    serialize = CarSerializer(data=JSONParser().parse(io.BytesIO(json)))
    return serialize.save() if serialize.is_valid() else ""
