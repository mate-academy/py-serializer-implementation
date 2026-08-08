import io

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    return JSONRenderer().render(CarSerializer(car).data)


def deserialize_car_object(json: bytes) -> Car:
    serializer = CarSerializer(data=JSONParser().parse(io.BytesIO(json)))
    serializer.is_valid()
    serializer.save()

    return serializer.instance
