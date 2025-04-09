from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io

from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    car_serializer = CarSerializer(car)
    return JSONRenderer().render(car_serializer.data)


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    car_serializer = CarSerializer(data=JSONParser().parse(stream))
    car_serializer.is_valid(raise_exception=True)

    return car_serializer.save()
