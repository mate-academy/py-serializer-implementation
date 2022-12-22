from car.models import Car
from car.serializers import CarSerializer
# from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(data=car)
    return serializer.data


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    return JSONParser().parse(stream)
